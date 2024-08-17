let signUp = document.getElementById("signUp");
let signIn = document.getElementById("signIn");
let nameInput = document.getElementById("nameInput");
let title = document.getElementById("title");

signIn.onclick = function(){
    nameInput.style.maxHeight = "0";
    title.innerHTML = "Login";
    signUp.classList.add("disable");
    signIn.classList.remove("disable");
}

console.log("El archivo JavaScript está conectado correctamente");
signUp.onclick = function(){
    nameInput.style.maxHeight = "60px";
    title.innerHTML = "FixFast";
    signUp.classList.remove("disable");
    signIn.classList.add("disable");
}
