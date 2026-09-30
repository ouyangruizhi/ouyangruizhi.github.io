// Year is primary; both header controls retain their own sort direction.
const awardTable = document.querySelector('#awards-list');
if (awardTable) {
  const descending = {year: true, rank: true};
  const buttons = [...awardTable.querySelectorAll('.award-sort')];
  const language = document.documentElement.lang.startsWith('zh') ? 'zh' : 'en';
  for (const button of buttons) {
    button.addEventListener('click', () => {
      descending[button.dataset.sort] = !descending[button.dataset.sort];
      const rows = [...awardTable.querySelectorAll('article.award')];
      rows.sort((a, b) => {
        const year = Number(b.dataset.year) - Number(a.dataset.year);
        const level = Number(b.dataset.rank) - Number(a.dataset.rank) || Number(a.dataset.prize) - Number(b.dataset.prize);
        return (descending.year ? year : -year) || (descending.rank ? level : -level);
      });
      for (const row of rows) awardTable.append(row);
      for (const control of buttons) {
        const down = descending[control.dataset.sort];
        control.parentElement.setAttribute('aria-sort', down ? 'descending' : 'ascending');
        control.querySelector('.sort-icon').textContent = down ? '↓' : '↑';
      }
      const label = language === 'zh'
        ? `年份${descending.year ? '从新到旧' : '从旧到新'}，同年按级别${descending.rank ? '从高到低' : '从低到高'}`
        : `Year ${descending.year ? 'newest first' : 'oldest first'}, then distinction ${descending.rank ? 'highest first' : 'lowest first'}`;
      awardTable.setAttribute('aria-description', label);
    });
  }
}
