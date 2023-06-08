
let myArr = localStorage.getItem("arrDataStorage");
let arrData = JSON.parse(myArr);


let params = (new URL(document.location)).searchParams;
let index = params.get("index");

let student = arrData[index];



let formElement = document.getElementById("depStudentForm");

document.getElementById("name").value = student.name;
document.getElementById("ID").value = student.IDnum;
document.getElementById("dep").value = student.dep;


function assing(e) {
    e.preventDefault();
    if (student.level >= 2) {
        e.preventDefault();
        student.dep = document.getElementById('dep').value,




            localStorage.setItem("arrDataStorage", JSON.stringify(arrData));
        window.location.href = "student_list.html";
    }
    else {
        alert("level not enough")
        // window.location.href = "student_list.html";
    }

}

document.getElementById("save").addEventListener("click", assing);