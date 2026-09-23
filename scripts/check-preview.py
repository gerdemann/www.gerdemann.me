#!/usr/bin/env python3
"""Check a running local preview, including legacy routes and page resources."""
import argparse
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids, self.references, self.external_loads, self.meta = set(), [], [], {}
        self.h1 = 0
        self.lang = None
        self.canonical = None
        self.feed(source)
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get('id'): self.ids.add(a['id'])
        if tag == 'h1': self.h1 += 1
        if tag == 'html': self.lang = a.get('lang')
        if tag == 'meta': self.meta[a.get('name', a.get('property'))] = a.get('content', '')
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical = a.get('href')
        if tag in ('a', 'link') and a.get('href'): self.references.append(a['href'])
        if tag in ('img', 'script', 'iframe', 'source'):
            if a.get('src'): self.references.append(a['src'])
            if a.get('srcset'):
                self.references.extend(part.strip().split()[0] for part in a['srcset'].split(','))
            if a.get('src', '').startswith(('https://', '//')): self.external_loads.append(a['src'])

parser = argparse.ArgumentParser()
parser.add_argument('--base-url', default='http://127.0.0.1:1313/')
args = parser.parse_args()
base = args.base_url.rstrip('/') + '/'
if urllib.parse.urlsplit(base).hostname not in ('127.0.0.1', 'localhost'):
    sys.exit('Only a local preview may be checked.')
legacy = json.loads((ROOT / 'docs/legacy-urls.json').read_text())
redirects = json.loads((ROOT / 'docs/redirects.json').read_text())
errors, cache = [], {}

class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl): return None
opener = urllib.request.build_opener(NoRedirect)
def fetch(path):
    url = urllib.parse.urljoin(base, path)
    try:
        response = opener.open(url, timeout=10)
        return response.status, response.headers, response.read()
    except urllib.error.HTTPError as error:
        return error.code, error.headers, error.read()

def load(row):
    return row['url'], fetch(row['url'])
with ThreadPoolExecutor(max_workers=8) as pool:
    cache.update(pool.map(load, legacy))

pages = {}
for row in legacy:
    path = row['url']
    status, headers, body = cache[path]
    if path in redirects:
        if status != 301 or urllib.parse.urlsplit(headers.get('Location', '')).path != redirects[path]:
            errors.append(f'Wrong redirect: {path}: {status} {headers.get("Location")}')
        target = redirects[path]
        if target not in cache: cache[target] = fetch(target)
        if cache[target][0] != 200: errors.append(f'Redirect target missing: {target}')
        continue
    if status != 200: errors.append(f'Legacy URL: {path}: HTTP {status}')
    if 'text/html' in headers.get('Content-Type', '') and status == 200:
        source = body.decode()
        page = Page(source)
        pages[path] = page
        if page.h1 != 1: errors.append(f'{path}: expected one h1, got {page.h1}')
        if page.lang != 'de': errors.append(f'{path}: wrong UI language')
        if not page.meta.get('description'): errors.append(f'{path}: missing description')
        if not page.canonical or not page.canonical.startswith(base): errors.append(f'{path}: non-local canonical')
        if path.startswith('/posts/') and row['headings'] and 'class="article-meta"' not in source: errors.append(f'{path}: article template missing')
        if 'noindex' not in page.meta.get('robots', ''): errors.append(f'{path}: indexable preview')
        if page.external_loads: errors.append(f'{path}: external resources {page.external_loads}')
        if 'tracking.gerdemann.me' in source or 'src="https://giscus.' in source: errors.append(f'{path}: tracking/comments enabled')
        missing = set(row['headings']) - page.ids
        if missing: errors.append(f'{path}: missing old anchors: {missing}')
    elif path.endswith('.xml') and status == 200:
        try: ET.fromstring(body)
        except ET.ParseError as error: errors.append(f'{path}: invalid XML: {error}')

references = set()
for path, page in pages.items():
    for ref in page.references:
        resolved = urllib.parse.urlsplit(urllib.parse.urljoin(urllib.parse.urljoin(base, path), ref))
        if resolved.netloc == urllib.parse.urlsplit(base).netloc:
            references.add((resolved.path or '/', urllib.parse.unquote(resolved.fragment)))
        elif resolved.hostname in ('gerdemann.me', 'www.gerdemann.me'):
            errors.append(f'{path}: internal link leaves preview: {ref}')
for path, fragment in sorted(references):
    if path not in cache: cache[path] = fetch(path)
    status, headers, body = cache[path]
    if status == 301 and path == '/index.html' and headers.get('Location') == './': continue
    if status != 200: errors.append(f'Internal resource: {path}: HTTP {status}')
    elif fragment and 'text/html' in headers.get('Content-Type', ''):
        if fragment not in Page(body.decode()).ids: errors.append(f'Broken fragment: {path}#{fragment}')

if fetch('/this-page-does-not-exist-acceptance.html')[0] != 404:
    errors.append('Missing pages must return HTTP 404.')
feed = ET.fromstring(cache['/feed.xml'][2])
items = feed.findall('./channel/item')
expected_articles = list((ROOT / 'content/posts').rglob('*.md'))
expected_articles = [p for p in expected_articles if p.name != '_index.md' and 'draft: true' not in p.read_text()]
if len(items) != len(expected_articles): errors.append(f'RSS count: {len(items)} instead of {len(expected_articles)}')
if errors:
    print('\n'.join(sorted(set(errors))))
    sys.exit(1)
print(f'PASS: {len(legacy)} legacy URLs, {len(redirects)} permanent redirects, {len(pages)} HTML pages, {len(references)} internal links/assets, {len(items)} RSS entries; local resources, old anchors, metadata, and 404 verified.')
