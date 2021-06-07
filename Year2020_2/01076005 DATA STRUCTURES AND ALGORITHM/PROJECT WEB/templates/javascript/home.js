/* onclick="myFunction()" */
function myFunction1() {
    /*document.body.style.backgroundColor = "yellow";*/
    document.body.style.backgroundImage = "url(images/home_BG1.jpg)";
    $("#about").show();
    $("#rooms").hide();
    $("#contact").hide();
}
function myFunction2() {
    document.body.style.backgroundImage = "url(images/home_BG2.jpg)";
    $("#about").hide();
    $("#rooms").show();
    $("#contact").hide();
    $(this).hide()
}
function myFunction4() {
    document.body.style.backgroundImage = "url(images/home_BG3.jpg)";
    $("#about").hide();
    $("#rooms").hide();
    $("#contact").show();
}
$(document).ready(function () {
    $("#about").show();
    $("#rooms").hide();
    $("#contact").hide();
});