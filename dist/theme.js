// Apply before the body is painted to avoid a flash of the wrong theme.
(() => {
  const key = 'homepage-theme';
  const root = document.documentElement;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const normalize = value => ['light', 'dark'].includes(value) ? value : 'system';
  const chinese = root.lang.startsWith('zh');
  let preference = 'system';
  try { preference = normalize(localStorage.getItem(key)); } catch (_) {}

  function apply() {
    root.dataset.theme = preference === 'system'
      ? (system.matches ? 'dark' : 'light') : preference;
    const control = document.getElementById('theme-toggle');
    if (!control) return;
    const dark = root.dataset.theme === 'dark';
    const label = chinese
      ? `当前${dark ? '深色' : '浅色'}，点击切换${dark ? '浅色' : '深色'}`
      : `Currently ${dark ? 'dark' : 'light'}; switch to ${dark ? 'light' : 'dark'} theme`;
    control.setAttribute('aria-label', label);
    control.title = label + (preference === 'system'
      ? (chinese ? '（跟随系统）' : ' (following system)')
      : (chinese ? '；按 Esc 跟随系统' : '; press Esc to follow system'));
  }

  function save() {
    try {
      if (preference === 'system') localStorage.removeItem(key);
      else localStorage.setItem(key, preference);
    } catch (_) {}
    apply();
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
    const control = document.getElementById('theme-toggle');
    if (!control) return;
    apply();
    control.addEventListener('click', () => {
      preference = root.dataset.theme === 'dark' ? 'light' : 'dark';
      save();
    });
    control.addEventListener('keydown', event => {
      if (event.key === 'Escape') {
        preference = 'system';
        save();
      }
    });
  });
})();
