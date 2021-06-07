/*https://www.youtube.com/watch?v=8zQb8Nktt50*/

const toggle = () => {
    let password = document.getElementById("password");
    let eye1 = document.getElementById("toggleeye1");
    let eye2 = document.getElementById("toggleeye2");

    if (password.type === "password"){
        password.type = "text";
        eye2.style.display = "none";
        eye1.style.color = "rgb(60, 179, 113)";
        eye1.style.display = "block";
    } else {
        password.type = "password";
        eye2.style.display = "block";
        eye1.style.color = "rgb(90, 90, 90)"
        eye1.style.display = "none";
    }
}
