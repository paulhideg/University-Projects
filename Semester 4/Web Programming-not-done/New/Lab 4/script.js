const table = document.querySelector("table");

table.addEventListener("click", sortColumn);

function sortColumn(event) {
  const clickedElement = event.target;
  if (clickedElement.tagName !== "TH") return;

  const columnIndex = clickedElement.cellIndex;
  const tableBody = table.querySelector("tbody");
  const tableRows = Array.from(tableBody.querySelectorAll("tr"));
  console.log(tableRows);

  tableRows.sort((rowA, rowB) => {
    const cellA = rowA.querySelectorAll("td")[columnIndex].textContent;
    const cellB = rowB.querySelectorAll("td")[columnIndex].textContent;
    return cellA.localeCompare(cellB);
  });

  let sortOrder = clickedElement.getAttribute("data-sort") || "asc";
  sortOrder = sortOrder === "asc" ? "desc" : "asc";
  clickedElement.setAttribute("data-sort", sortOrder);

  if (sortOrder === "desc") {
    tableRows.reverse();
  }
  tableRows.forEach((row) => {
    const cells = row.querySelectorAll("td");
    for (let i = 0; i < cells.length; i++) {
      i != columnIndex
        ? (cells[i].style.backgroundColor = "white")
        : (cells[i].style.backgroundColor =
            cells[columnIndex].style.backgroundColor === "green"
              ? "blue"
              : "green");
    }
  });

  tableBody.innerHTML = "";
  tableRows.forEach((row) => tableBody.appendChild(row));
}
