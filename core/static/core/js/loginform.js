const loginform = document.forms['loginform'];

const id_userlogin = document.getElementById("id_username")
const id_passwordlogin = document.getElementById("id_password")




function validateInputsLogin() {

    const iduserValue = id_user.value.trim();


    if (id_userlogin === '') {
        alert('Por favor, completa el campo de nombre de usuario.');
        return false;  
    } else if (id_userlogin.length > 30) {
        alert('El Nombre de usuario no debe tener más de 30 caracteres.');
        return false;  
    } 



    return true; 
}

document.addEventListener('DOMContentLoaded', function() {
    // Tu código aquí
    loginform.addEventListener('submit', function (event) {
        if (!validateInputsLogin()) {
            event.preventDefault();  // Previene el envío del formulario si hay un error
        }
    });
});
