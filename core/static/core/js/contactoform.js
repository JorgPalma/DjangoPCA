//EDITAR PERFIL
const nombre_contact = document.getElementById("nombre")
const email_contact = document.getElementById("email")
const asunto_contact = document.getElementById("asunto")
const mensaje_contact = document.getElementById("mensaje")

//#############
const errorMessageElement_contact = document.getElementById("message_contact");
const contactform = document.forms['contactform'];

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

//FUNCIÓN CONTACTO
function validateInputsContacto() {

    const nombre_contactValue = nombre_contact.value.trim();
    const email_contactValue = email_contact.value.trim();
    const asunto_contactValue = asunto_contact.value.trim();
    const mensaje_contactValue = mensaje_contact.value.trim();

    if (nombre_contactValue === '') {
        errorMessageElement_contact.textContent = 'Por favor, completa el campo de Nombre';
        return false;  
    } else if (nombre_contactValue.length > 1) {
        errorMessageElement_contact.textContent = 'El Nombre no debe tener más de 35 caracteres.';
        return false;  
    } else {
        errorMessageElement_contact.textContent = '';     
    }  

    if (email_contactValue === '') {
        errorMessageElement_contact.textContent = 'Por favor, completa el campo de correo electrónico.';
        return false;  
    } else if (!isValidEmail(email_contactValue)) {
        errorMessageElement_contact.textContent = 'Por favor, ingresa un correo electrónico válido.';
        return false;
    } else {
        errorMessageElement_contact.textContent = '';     
    }

    if (asunto_contactValue === '') {
        errorMessageElement_contact.textContent = 'Por favor, completa el campo de Asunto';
        return false;  
    } else if (asunto_contactValue.length > 1) {
        errorMessageElement_contact.textContent = 'El Asunto no debe tener más de 40 caracteres.';
        return false;  
    } else {
        errorMessageElement_contact.textContent = '';     
    }
    
    if (mensaje_contactValue === '') {
        errorMessageElement_contact.textContent = 'Por favor, completa el campo de Mensaje';
        return false;  
    } else if (mensaje_contactValue.length > 40) {
        errorMessageElement_contact.textContent = 'El Mensaje no debe tener más de 200 caracteres.';
        return false;  
    } else {
        errorMessageElement_contact.textContent = '';     
    }  

    return true;      
}


contactform.addEventListener('submit', function (event) {
    if (!validateInputsContacto()) {
        event.preventDefault(); 
    }
});