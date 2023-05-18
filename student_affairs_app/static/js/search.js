

var arrDataStorage = JSON.parse(localStorage.getItem("arrDataStorage")) || [];

const tableBody = document.getElementById("tableBodySearch")
let index = 0;
for (const student of arrDataStorage) {
    const row = document.createElement('tr');
    const nameCell = document.createElement('td');
    const idCell = document.createElement('td');
    const dobCell = document.createElement('td');
    const gpaCell = document.createElement('td');
    const levelCell = document.createElement('td');
    const deptCell = document.createElement('td');
    const genderCell = document.createElement('td');
    const emailCell = document.createElement('td');
    const phoneCell = document.createElement('td');
    const statusCell = document.createElement('td');
    var editButton = document.createElement("button");
    var changeDepartmentButton = document.createElement("button");
    var editCell = document.createElement("td");
    var changeDepartmentCell = document.createElement("td");
    editButton.setAttribute("onclick", `editfn(${index})`);
    changeDepartmentButton.setAttribute("onclick", `depfn(${index})`);
    index++;

    nameCell.textContent = student.name;
    idCell.textContent = student.IDnum;
    dobCell.textContent = student.birthDate;
    gpaCell.textContent = student.gpa;
    levelCell.textContent = student.level;
    deptCell.textContent = student.dep;
    genderCell.textContent = student.gender;
    emailCell.textContent = student.email;
    phoneCell.textContent = student.mobile;
    statusCell.textContent = student.status;
    editButton.textContent = "Edit info";
    changeDepartmentButton.textContent = "Edit Department";
    editButton.classList.toggle("btn");
    changeDepartmentButton.classList.toggle("btn");



    // add row to table body
    row.appendChild(nameCell);
    row.appendChild(idCell);
    row.appendChild(dobCell);
    row.appendChild(gpaCell);
    row.appendChild(levelCell);
    row.appendChild(deptCell);
    row.appendChild(genderCell);
    row.appendChild(emailCell);
    row.appendChild(phoneCell);
    row.appendChild(statusCell);
    row.appendChild(editCell);
    row.appendChild(changeDepartmentCell);
    editCell.appendChild(editButton);
    editButton.id = "editButton";
    changeDepartmentCell.appendChild(changeDepartmentButton);
    changeDepartmentButton.id = "changeDepartmentButton";

    tableBody.appendChild(row);

    function editfn(index) {
        window.location.href = "edit_student.html?index=" + index;
    };


    function depfn(index) {
        window.location.href = "assign_department.html?index=" + index;
    }

}








let column = document.getElementById("searchType");

let indx = 0;
column.addEventListener("change", function () {
    switch (column.value) {
        case "name":
            indx = 0;
            break;
        case "id":
            indx = 1;
            break;
        case "department":
            indx = 5;
            break;
        default:
            indx = 0;
    }
})

const searchInput = document.getElementById("myInput");
const tableBodysh = document.getElementById("tableBodySearch");

searchInput.addEventListener("input", function () {
    let rows = tableBodysh.getElementsByTagName("tr")
    for (let i = 0; i < rows.length; i++) {
        let rowData = rows[i].getElementsByTagName("td")
        let cellData = rowData[indx].textContent.toLowerCase();
        // console.log(searchInput.value)
        if (cellData.indexOf(searchInput.value.toLowerCase()) > -1) {
            rows[i].style.display = "";
        }
        else {
            rows[i].style.display = "none";
        }
    }

})


