# Michael Gerdemann – lokale Portfolio-Vorschau

Die neue Oberfläche läuft mit Hugo und Markdown. Sie umfasst eine Portfolio-Startseite,
ein deutsches Profil, das Blogarchiv und die bestehenden Artikel in ihrer Originalsprache.
Das bisherige Theme-Submodul bleibt als Referenz vorhanden, wird aber nicht mehr eingebunden.

## Voraussetzungen

Auf diesem Mac wurde Hugo **0.166.0 extended** installiert. Zusätzlich wird Python 3 benötigt.

```sh
brew install hugo
```

## Vorschau starten

Im Projektverzeichnis:

```sh
./scripts/preview.sh
```

Das Skript bindet den Server ausschließlich an `127.0.0.1`. Es verwendet Port 1313,
bei Belegung den nächsten freien Port bis 1349. Die tatsächliche Adresse steht in der
Terminalausgabe. Interne Links und Assets verwenden die lokale Adresse.

`preview.toml` deaktiviert Matomo und Giscus und setzt `noindex` sowie `robots.txt` auf
Ausschluss der Vorschau. YouTube-Videos sind externe Links; sie laden nicht automatisch.
Hell-/Dunkelmodus verwendet zunächst die Systemeinstellung und speichert eine manuelle
Auswahl lokal im Browser.

## Vorschau beenden

Im laufenden Terminal **Ctrl+C** drücken. Falls die Vorschau im Hintergrund läuft:

```sh
python3 scripts/stop-preview.py
```

Das Stoppskript prüft, ob die gespeicherte Prozess-ID zu einem lokalen Hugo-Vorschauprozess
gehört. Nach einem Neustart des Macs muss die Vorschau erneut gestartet werden.

## Prüfen

Bei laufender Vorschau:

```sh
python3 scripts/check-preview.py
# Bei abweichendem Port:
python3 scripts/check-preview.py --base-url http://127.0.0.1:1314/
```

Der Check kontrolliert alte URLs, permanente Weiterleitungen, Überschriftenanker,
interne Links/Bilder/Skripte, Metadaten, RSS, deaktivierte externe Einbindungen und 404.

Ein separater lokaler Build:

```sh
hugo --config config.toml,preview.toml --baseURL http://127.0.0.1:1313/ --destination /tmp/gerdemann-preview-build --cleanDestinationDir
```

## Inhalte und Gestaltung bearbeiten

- Profil: `content/about.md`
- Projekte: `data/projects.toml` (Name, Kategorie, Beschreibung, Beitrag, URL, Linktext und Illustration)
- Beiträge: `content/posts/`; `articleLanguage: de` bzw. `en` kennzeichnet die Inhaltssprache, ohne die URL zu verändern.
- Ein beitragsspezifisches Social-Media-Bild kann im Frontmatter mit `socialImage` gesetzt werden. Bei Page Bundles wird andernfalls automatisch ein vorhandenes PNG oder JPG verwendet.
- Gestaltung: `assets/css/site.css`; Interaktion: `assets/js/site.js`
- Eigene Hugo-Templates: `layouts/`

Das MG-Zeichen im Header liegt in `layouts/partials/brand-mark.html`. Favicon,
Touch- und Android-Icons, Safari-Maske und Social Preview werden aus denselben
Buchstabenformen erzeugt. Zum erneuten Export auf diesem Mac werden `rsvg-convert`
und `fonttools` benötigt:

```sh
uv run --no-project --with fonttools python scripts/generate-brand-assets.py
```

Projektgrafiken sind typografische Illustrationen, keine Screenshots der Apps.
Das Profil wurde mit öffentlichen Angaben von LinkedIn, XING, VARIOS AI, GitHub und dem
App Store aktualisiert. Die Belege und Grenzen stehen in `docs/profile-research.md`.

## Alte Adressen

`docs/legacy-urls.json` enthält die vor dem Umbau erfassten 196 Seiten-, Feed- und
Bild-URLs samt Überschriftenankern. Die Vergleichsbasis wurde aus dem unveränderten
Repository mit Hugo 0.120.4 einschließlich Entwürfen erzeugt. Alte Theme-CSS/JS-Dateien
sind nicht Teil der Inhalts-URL-Garantie.

Alle Artikelpfade bleiben erhalten. Das bewahrt auch die pfadbasierte Giscus-Zuordnung.
45 frühere Paginierungs-URLs führen mit HTTP 301 zum vollständigen jeweiligen Archiv.
Die genaue Zuordnung steht in `docs/redirects.json`; die lokalen Regeln in `preview.toml`.
Alte generierte WebP-Dateien sind unter `static/posts/` erhalten, weil neuere Hugo-Versionen
andere Dateinamen generieren können.

## Produktionskonfiguration

Der Container baut mit Hugo 0.166.0 und liefert die Seite über
Nginx 1.30.5 aus. Die 45 historischen Weiterleitungen werden aus
`docs/legacy-redirects.nginx.conf` eingebunden. Sicherheitsheader begrenzen Skripte, Frames,
Referrer und Browserberechtigungen; HSTS wird am Traefik-TLS-Endpunkt gesetzt.

Matomo ist vollständig entfernt. Giscus wird in der Produktionsfassung erst nach einem
Klick auf „Kommentare laden“ eingebunden. Die Deployment-Actions sind auf geprüfte
Release-Commits festgeschrieben, und das Rancher-Hostlabel lautet `hetzner`.

Bei Änderungen am Host muss das Hostlabel mit der tatsächlichen Rancher-Konfiguration
übereinstimmen. Nach jedem Deployment sind Weiterleitungen, Sicherheitsheader und die
Kommentar-Einwilligung gegen die öffentliche Adresse zu prüfen.
