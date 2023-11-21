const registroform = document.forms['registroform'];

const id_user = document.getElementById("id_username")
const id_user_email = document.getElementById("id_email")
const id_user_password1 = document.getElementById("id_password1")
const id_user_password2 = document.getElementById("id_password2")

function isValidEmail_registro(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function validateInputsRegistro() {

    const iduserValue = id_user.value.trim();
    const iduser_emailValue = id_user_email.value.trim();
    const iduser_password1Value = id_user_password1.value.trim();
    const iduser_password2Value = id_user_password2.value.trim();

    if (iduserValue === '') {
        alert('Por favor, completa el campo de nombre de usuario.');
        return false;  
    } else if (iduserValue.length > 30) {
        alert('El Nombre de usuario no debe tener más de 30 caracteres.');
        return false;  
    } 

    if (iduser_emailValue === '') {
        alert('Por favor, completa el campo de correo electrónico.');
        return false;  
    } else if (!isValidEmail_registro(iduser_emailValue)) {
        alert('Por favor, ingresa un correo electrónico válido.');
        return false;
    }

    if (iduser_password1Value === '') {
        alert('Por favor, completa el campo de contraseña.');
        return false;  
    } else if (iduser_password1Value.length > 30) {
        alert('La contraseña no debe tener más de 30 caracteres.');
        return false;  
    } 

    if (iduser_password2Value === '') {
        alert('Por favor, completa el campo de confirmación de contraseña.');
        return false;  
    } else if (iduser_password2Value.length > 30) {
        alert('La contraseña no debe tener más de 30 caracteres.');
        return false;  
    } 


    return true; 
}

document.addEventListener('DOMContentLoaded', function() {
    // Tu código aquí
    registroform.addEventListener('submit', function (event) {
        if (!validateInputsRegistro()) {
            event.preventDefault();  // Previene el envío del formulario si hay un error
        }
    });
});
