// Apply before the body is painted to avoid a flash of the wrong theme.
(() => {
  const key = 'homepage-theme';
  const root = document.documentElement;
  const system = window.matchMedia('(prefers-color-scheme: dark)');
  const normalize = value => ['light', 'dark'].includes(value) ? value : 'system';
  let preference = 'system';
  try { preference = normalize(localStorage.getItem(key)); } catch (_) {}

  function apply() {
    root.dataset.theme = preference === 'system'
      ? (system.matches ? 'dark' : 'light') : preference;
    const control = document.getElementById('theme-switch');
    if (control) control.value = preference;
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
    const control = document.getElementById('theme-switch');
    if (!control) return;
    apply();
    control.addEventListener('change', () => {
      preference = normalize(control.value);
      try {
        if (preference === 'system') localStorage.removeItem(key);
        else localStorage.setItem(key, preference);
      } catch (_) {}
      apply();
    });
  });
})();
