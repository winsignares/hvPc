

// Función para validar el correo y la contraseña
 function validarlogin() {
    const nameuser= document.getElementById("emailuser").value;
    const passuser= document.getElementById("passuser").value;
  try {
      axios.post('validarlogin', {
      email: nameuser,
      password: passuser
    });

    // Verificar la respuesta del servidor
    if (respuesta.data.valido) {
      console.log('Las credenciales son válidas.');
    } else {
      console.log('Las credenciales no son válidas.');
    }
  } catch (error) {
    console.error('Error al validar las credenciales:', error.message);
  }
}