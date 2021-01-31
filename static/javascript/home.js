window.onload = function() {
    homeCount();
};

function homeCount() {
    var memberCount = document.getElementById("memberCount");
    memberCount.innerText = "0"
    fetch('http://127.0.0.1:8000/alluser/')
        .then(function(response) {
            return response.json();
        }).then(function(data) {
            memberCount.innerText = data.length
        });
}