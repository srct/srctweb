function checkDate() {
    var d = new Date(),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate()
    if (month == 3 && day > 20) {
        var body = document.getElementById("body");
        body.classList.add("pride-bar");
    }
}
window.onload = checkDate