$(document).ready(() => {
    $('#tracker-table').dataTable({
        scrollX: true,
        scrollY: 400,
        columnDefs: [{
          orderable: false,
          className: 'select-checkbox select-checkbox-all',
          targets: 0
        }],
        select: {
          style: 'multi',
          selector: 'td:first-child'
        }
    });
});