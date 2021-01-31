function loginCheck() {
    var email = document.getElementById("email").value
    var pwd = document.getElementById("pwd").value
    fetch('http://localhost:8000/alluser/')
        .then(function(response) {
            return response.json()
        }).then(function(data) {
            console.log(data)
        });
}