function signup(e) {
    e.preventDefault();
    var email = document.getElementById("email").value
    var pwd = document.getElementById("pwd").value
    var confrimPwd = document.getElementById("cfmpwd").value
    var role = document.getElementById("acc").value
    if (pwd === confrimPwd) {
        const postData = {
            "email_id": email,
            "first_name": "null",
            "last_name": "null",
            "role": role,
            "password": confrimPwd
        }
        fetch('/alluser/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json; charset=UTF-8' },
            body: JSON.stringify(postData)
        }).then(function(response) {
            return response.json();
        }).then(function(data) {
            console.log('Created User:', data);
            window.location = "/pro1"
        });
    }
}



function createUser() {
    var opts = {
        "first_name": "Fstudent1",
        "last_name": "Lstudent1",
        "email_id": null,
        "phone": null,
        "address": null,
        "role": "1",
        "seek_skills": null,
        "teach_skills": null,
        "country": null,
        "rate": null,
        "rating": null,
        "level": null,
        "Languages": null,
        "password": null
    }
    fetch('http://localhost:8000/alluser/', {
        method: 'post',
        body: JSON.stringify(opts)
    }).then(function(response) {
        return response.json();
    }).then(function(data) {
        console.log('Created User:', data.first_name);
    });
}