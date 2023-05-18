
// Retrieve the student data from local storage
const studentData = JSON.parse(localStorage.getItem('arrDataStorage')) || [];

// Get the table body element
const tableBody = document.getElementById('tableBodyList');

// Loop through the student data and generate table rows for each student
for (const student of studentData) {
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
    tableBody.appendChild(row);
}
