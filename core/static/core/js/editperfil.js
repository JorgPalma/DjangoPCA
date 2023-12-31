//EDITAR PERFIL
const primer_nombre = document.getElementById("p_nombre")
const segundo_nombre = document.getElementById("s_nombre")
const apellido_pat = document.getElementById("p_apellido")
const apellido_mate = document.getElementById("m_apellido")
const id_rut = document.getElementById("rut")
const id_digito_ver = document.getElementById("dv")
const id_telefono = document.getElementById("telefono")
const id_edad = document.getElementById("edad")
const id_imagen = document.getElementById("id_imagen")


//#############
const errorMessageElement = document.getElementById("error-message");
const editForm = document.forms['editform'];

function isValidEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

//FUNCIÓN EDITAR PERFIL
function validateInputsEditarPerfil() {

    const primerNombreValue = primer_nombre.value.trim();
    const segundoNombreValue = segundo_nombre.value.trim();
    const primerApellidoValue = apellido_pat.value.trim();
    const segundoApellidoValue = apellido_mate.value.trim();
    const rutValue = id_rut.value.trim();
    const digitoValue = id_digito_ver.value.trim();
    const telefonoValue = id_telefono.value.trim();
    const edadValue = id_edad.value.trim();

    if (primerNombreValue === '') {
        errorMessageElement.textContent = 'Por favor, completa el campo del primer nombre.';
        return false;  
    } else if (primerNombreValue.length > 25) {
        errorMessageElement.textContent = 'El Primer Nombre no debe tener más de 25 caracteres.';
        return false;  
    } else {
        errorMessageElement.textContent = '';     
    }  

    if (segundoNombreValue.length > 25) {
        errorMessageElement.textContent = 'El Segundo Nombre no debe tener más de 25 caracteres.';
        return false;  
    } else {
        errorMessageElement.textContent = '';      
    }

    if (primerApellidoValue === '') {
        errorMessageElement.textContent = 'Por favor, completa el campo del primer apellido.';
        return false;  
    } else if (primerApellidoValue.length > 25) {
        errorMessageElement.textContent = 'El Primer Apellido no debe tener más de 25 caracteres.';
        return false;  
    } else {
        errorMessageElement.textContent = '';     
    }

    if (segundoApellidoValue.length > 25) {
        errorMessageElement.textContent = 'El Segundo Apellido no debe tener más de 25 caracteres.';
        return false;  
    } else {
        errorMessageElement.textContent = '';      
    }

    if (rutValue === '') {
        errorMessageElement.textContent = 'Por favor, completa el campo del rut.';
        return false;  
    } else if (rutValue.length > 8) {
        errorMessageElement.textContent = 'El rut no debe tener más de 8 caracteres.';
        return false; 
    } else if (rutValue.length < 7) {
        errorMessageElement.textContent = 'El rut no debe tener menos de 7 caracteres.';
        return false;  
    } else {
        errorMessageElement.textContent = '';     
    }

    if (!/^[0-9kK]{1}$/.test(digitoValue)) {
        errorMessageElement.textContent = 'El dígito verificador solo puede ser un número del 0 al 9 o la letra "k".';
        return false;
    }else if (digitoValue === '') {
            errorMessageElement.textContent = 'Por favor, completa el campo del digito verificador.';
            return false;  
    }else {
        errorMessageElement.textContent = '';     
    }

    if (telefonoValue === '') {
        errorMessageElement.textContent = 'Por favor, completa el campo de numero de telefono.';
        return false;  
    } else if (telefonoValue.length > 9) {
        errorMessageElement.textContent = 'El numero de telefono no debe tener más de 9 numeros.';
        return false; 
    } else if (telefonoValue.length < 9) {
        errorMessageElement.textContent = 'El numero de telefono no debe tener menos de 9 numeros.';
        return false;  
    } else {
        errorMessageElement.textContent = '';     
    }

    if (edadValue === '') {
        errorMessageElement.textContent = 'Por favor, completa el campo de edad.';
        return false;  
    } else if (edadValue.length > 3) {
        errorMessageElement.textContent = 'La edad no debe tener más de 3 caracteres.';
        return false; 
    } else {
        errorMessageElement.textContent = '';     
    }

    return true;  
}




document.addEventListener('DOMContentLoaded', function() {
    // Tu código aquí
    editForm.addEventListener('submit', function (event) {
        if (!validateInputsEditarPerfil()) {
            event.preventDefault();  // Previene el envío del formulario si hay un error
        }
    });
});

