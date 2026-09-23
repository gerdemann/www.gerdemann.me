(() => {
  const root = document.documentElement;
  root.classList.add('js');
  document.querySelectorAll('.prose pre').forEach(block => {
    block.tabIndex = 0;
    block.setAttribute('aria-label', 'Codebeispiel');
  });
  const toggle = document.querySelector('.theme-toggle');
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)');
  function syncComments() {
    const frame = document.querySelector('iframe.giscus-frame');
    if (frame) frame.contentWindow.postMessage({ giscus: { setConfig: { theme: root.dataset.theme } } }, 'https://giscus.gerdemann.me');
  }
  function updateTheme(theme) {
    root.dataset.theme = theme;
    toggle.setAttribute('aria-pressed', String(theme === 'dark'));
    toggle.setAttribute('aria-label', theme === 'dark' ? 'Hellmodus aktivieren' : 'Dunkelmodus aktivieren');
    syncComments();
  }
  function setupComments() {
    const section = document.querySelector('.comments');
    const consent = section && section.querySelector('.comment-consent');
    const button = consent && consent.querySelector('.comment-load');
    const embed = section && section.querySelector('.comment-embed');
    if (!section || !consent || !button || !embed) return;

    button.addEventListener('click', () => {
      button.disabled = true;
      button.textContent = 'Kommentare werden geladen …';

      const script = document.createElement('script');
      const attributes = {
        src: button.dataset.clientSrc,
        'data-repo': button.dataset.repo,
        'data-repo-id': button.dataset.repoId,
        'data-category': button.dataset.category,
        'data-category-id': button.dataset.categoryId,
        'data-mapping': 'pathname',
        'data-reactions-enabled': '1',
        'data-emit-metadata': '0',
        'data-input-position': 'bottom',
        'data-theme': root.dataset.theme || 'preferred_color_scheme',
        'data-lang': 'de',
        crossorigin: 'anonymous'
      };

      Object.entries(attributes).forEach(([name, value]) => script.setAttribute(name, value));
      script.async = true;

      const observer = new MutationObserver(() => {
        const frame = embed.querySelector('iframe.giscus-frame');
        if (frame) {
          frame.addEventListener('load', syncComments);
          syncComments();
          observer.disconnect();
        }
      });
      observer.observe(embed, { childList: true, subtree: true });

      script.addEventListener('load', () => consent.remove());
      script.addEventListener('error', () => {
        observer.disconnect();
        script.remove();
        button.disabled = false;
        button.textContent = 'Kommentare erneut laden';
      });
      embed.appendChild(script);
    });
  }
  if (toggle) {
    toggle.hidden = false;
    updateTheme(root.dataset.theme);
    toggle.addEventListener('click', () => {
      const theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('theme', theme); } catch (_) {}
      updateTheme(theme);
    });
    systemTheme.addEventListener('change', event => {
      let saved = null;
      try { saved = localStorage.getItem('theme'); } catch (_) {}
      if (!saved) updateTheme(event.matches ? 'dark' : 'light');
    });
  }
  const menuButton = document.querySelector('.menu-toggle');
  const nav = document.querySelector('#hauptnavigation');
  if (menuButton && nav) {
    menuButton.hidden = false;
    function closeMenu() { nav.classList.remove('is-open'); menuButton.setAttribute('aria-expanded', 'false'); }
    menuButton.addEventListener('click', () => {
      const open = menuButton.getAttribute('aria-expanded') !== 'true';
      nav.classList.toggle('is-open', open);
      menuButton.setAttribute('aria-expanded', String(open));
    });
    nav.addEventListener('click', event => { if (event.target.closest('a')) closeMenu(); });
    document.addEventListener('keydown', event => {
      if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') { closeMenu(); menuButton.focus(); }
    });
  }
  setupComments();
})();
