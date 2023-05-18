document.getElementById("addStudentForm").addEventListener("submit", function (e) {
    e.preventDefault();
    let myArr = localStorage.getItem("arrDataStorage");
    if (myArr) {
        let myArrJson = JSON.parse(myArr);
        var formData = new FormData(e.target);
        let studentData = Object.fromEntries(formData);
        myArrJson.push(studentData);
        let arrDataStr = JSON.stringify(myArrJson);
        localStorage.setItem("arrDataStorage", arrDataStr);
    }
    else {
        var formData = new FormData(e.target);
        let studentData = Object.fromEntries(formData);
        let myArrJson = [studentData];
        let arrDataStr = JSON.stringify(myArrJson);
        localStorage.setItem("arrDataStorage", arrDataStr);
    }
    window.location.href = "student_list.html";
}
)
