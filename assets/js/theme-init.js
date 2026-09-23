(() => {
  const systemTheme = window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  try {
    document.documentElement.dataset.theme = localStorage.getItem('theme') || systemTheme;
  } catch (_) {
    document.documentElement.dataset.theme = systemTheme;
  }
})();
