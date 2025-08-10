document.addEventListener("DOMContentLoaded", function () {
  let lastSortedColumn = -1;
  let lastSortOrder = 'asc';
  let currentForm = null;

  //sortowanie
  function sortTable(columnIndex) {
    const table = document.querySelector('table');
    if (!table) return;

    const rows = Array.from(table.rows).slice(1);
    const isNumeric = columnIndex === 2;

    let sortOrder = (lastSortedColumn === columnIndex && lastSortOrder === 'asc') ? 'desc' : 'asc';
    lastSortedColumn = columnIndex;
    lastSortOrder = sortOrder;

    for (let i = 0; i < 4; i++) {
      const icon = document.getElementById(`sort-icon-${i}`);
      if (icon) icon.innerText = '';
    }

    const icon = document.getElementById(`sort-icon-${columnIndex}`);
    if (icon) icon.innerText = sortOrder === 'asc' ? '▲' : '▼';

    const sortedRows = rows.sort((a, b) => {
      const aText = a.cells[columnIndex].innerText.trim();
      const bText = b.cells[columnIndex].innerText.trim();

      if (isNumeric) {
        return sortOrder === 'asc' ? parseFloat(aText) - parseFloat(bText)
                                   : parseFloat(bText) - parseFloat(aText);
      } else {
        return sortOrder === 'asc' ? aText.localeCompare(bText)
                                   : bText.localeCompare(aText);
      }
    });

    for (const row of sortedRows) {
      table.tBodies[0].appendChild(row);
    }

    updateTotal();
  }

  //filtrowanie
  function filterTable() {
    const filterValue = document.getElementById('categoryFilter').value;
    const rows = document.querySelectorAll('table tbody tr');

    rows.forEach(row => {
      const category = row.cells[1].innerText.trim();
      row.style.display = (filterValue === 'all' || category === filterValue) ? '' : 'none';
    });

    updateTotal();
  }

  //sumowanie wydatków
  function updateTotal() {
    const rows = document.querySelectorAll('table tbody tr');
    let totalAmount = 0;

    rows.forEach(row => {
      if (row.style.display !== 'none') {
        const amount = parseFloat(row.cells[2].innerText);
        if (!isNaN(amount)) totalAmount += amount;
      }
    });

    const totalSpan = document.getElementById('totalAmount');
    if (totalSpan) totalSpan.innerText = totalAmount.toFixed(2);
  }

  //modal potwierdzenia usunięcia wydatku
  const modal = document.getElementById('custom-confirm');
  const yesBtn = document.getElementById('confirm-yes');
  const noBtn = document.getElementById('confirm-no');

  document.querySelectorAll('.delete-btn').forEach(button => {
    button.addEventListener('click', function (e) {
      e.preventDefault();
      currentForm = this.closest('form');
      modal.classList.remove('hidden');
    });
  });

  yesBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
    if (currentForm) currentForm.submit();
  });

  noBtn.addEventListener('click', () => {
    modal.classList.add('hidden');
    currentForm = null;
  });

  const categoryFilter = document.getElementById('categoryFilter');
  if (categoryFilter) categoryFilter.addEventListener('change', filterTable);

  const headers = document.querySelectorAll('th.sortable');
  headers.forEach((header, index) => {
    header.addEventListener('click', () => sortTable(index));
  });

  updateTotal();
});
