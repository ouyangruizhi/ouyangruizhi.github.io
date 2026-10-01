// Apply before the body is painted to avoid a flash of the wrong theme.
(() => {
  const key = 'homepage-theme';
  const root = document.documentElement;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const normalize = value => ['light', 'dark'].includes(value) ? value : 'system';
  let preference = 'system';
  const chinese = root.lang.startsWith('zh');
  try { preference = normalize(localStorage.getItem(key)); } catch (_) {}

  function apply() {
    root.dataset.theme = preference === 'system'
      ? (system.matches ? 'dark' : 'light') : preference;
    for (const control of document.querySelectorAll('[data-theme-option]')) {
      const mode = control.dataset.themeOption;
      const selected = preference === mode;
      const name = chinese ? (mode === 'light' ? '浅色' : '深色') : (mode === 'light' ? 'light' : 'dark');
      const label = selected
        ? (chinese ? `当前${name}主题，点击恢复跟随系统` : `Using ${name} theme; click to follow system`)
        : (chinese ? `切换${name}主题${preference === 'system' ? '（当前跟随系统）' : ''}` : `Use ${name} theme${preference === 'system' ? ' (currently following system)' : ''}`);
      control.setAttribute('aria-pressed', String(selected));
      control.setAttribute('aria-label', label);
      control.title = label;
      control.classList.toggle('is-current', mode === root.dataset.theme);
    }
  }

  apply();
  system.addEventListener('change', apply);
  window.addEventListener('storage', event => {
    if (event.key === key || event.key === null) {
      preference = normalize(event.newValue);
      apply();
    }
  });
  document.addEventListener('DOMContentLoaded', () => {
    apply();
    for (const control of document.querySelectorAll('[data-theme-option]')) {
      control.addEventListener('click', () => {
        preference = preference === control.dataset.themeOption ? 'system' : control.dataset.themeOption;
        try {
          if (preference === 'system') localStorage.removeItem(key);
          else localStorage.setItem(key, preference);
        } catch (_) {}
        apply();
      });
    }
  });
})();
