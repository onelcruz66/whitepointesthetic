
// Scripts for hiding and showing columns on a table.

function toggleColumn(columnIndex, elementId) {
    var table = document.getElementById(elementId);

    // Toggle the 'hidden' class for each cell in the specified column
    for (var i = 0, row; row = table.rows[i]; i++) {
        var cell = row.cells[columnIndex];
        cell.classList.toggle("hidden");
    }
}

function toggleAllColumns(elementId) {
    var table = document.getElementById(elementId);

    // Check if any cell in the table has the 'hidden' class
    var anyHidden = false;
    for (var i = 0, row; row = table.rows[i]; i++) {
        for (var j = 0, cell; cell = row.cells[j]; j++) {
            if (cell.classList.contains("hidden")) {
                anyHidden = true;
                break;
            }
        }
        if (anyHidden) {
            break;
        }
    }

    // Toggle the 'hidden' class for each cell in all columns
    for (var i = 0, row; row = table.rows[i]; i++) {
        for (var j = 0, cell; cell = row.cells[j]; j++) {
            cell.classList.toggle("hidden", !anyHidden);
        }
    }
    
}

// Event listener for hiding and showing columns on RequestedAppointments table.
document.addEventListener('DOMContentLoaded', function () {
    var headers = document.querySelectorAll('#data-table th');

    // Attach click event to each header
    headers.forEach(function (header, index) {
        header.addEventListener('click', function () {
            toggleColumn(index, "data-table");
        });
    });


    var toggleButton = document.getElementById('toggle-button');

    // Attach click event to the toggle button
    toggleButton.addEventListener('click', function () {
        toggleAllColumns("data-table");
    });
});

// Event listener for hiding and showing columns on ApprovedAppointments table.

document.addEventListener('DOMContentLoaded', function () {
    var headers = document.querySelectorAll('#data-table2 th');

    // Attach click event to each header
    headers.forEach(function (header, index) {
        header.addEventListener('click', function () {
            toggleColumn(index, "data-table2");
        });
    });


    var toggleButton = document.getElementById('toggle-button2');

    // Attach click event to the toggle button
    toggleButton.addEventListener('click', function () {
        toggleAllColumns("data-table2");
    });
});

// Event listener for hiding and showing columns on MessageRequest table.

document.addEventListener('DOMContentLoaded', function () {
    var headers = document.querySelectorAll('#data-table3 th');

    // Attach click event to each header
    headers.forEach(function (header, index) {
        header.addEventListener('click', function () {
            toggleColumn(index, "data-table3");
        });
    });


    var toggleButton = document.getElementById('toggle-button3');

    // Attach click event to the toggle button
    toggleButton.addEventListener('click', function () {
        toggleAllColumns("data-table3");
    });
});