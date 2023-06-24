// Función para validar el correo y la contraseña
function validarlogin() {
  const nameuser = document.getElementById("emailuser").value;
  const passuser = document.getElementById("passuser").value;

  console.log("getData.Email:'", nameuser, "'.and.Password:'", passuser, "'");

  axios
    .post("validarlogin", {
      email: nameuser,
      password: passuser
      
    }).then(function (response) {
        confirmarDatos()
        const data = response.data;
        if (data.message === 'Tus credenciales han expirado') {
            alert(data.message);
        } else {
            // Las credenciales son válidas, procesar el token, etc.
            const token = data.token;
            console.log(token);
            localStorage.setItem('token', token); // Almacena el token en el local storage
        console.log(response.data)}
        setTimeout(function(){

        window.location.href = "/fronted/indexhome"
        },4000 )
        
    })
    .catch((err) => {
        console.log(err)
        ErrorDatosLogin()
    })
}
function prevenir() {
  const login = document.getElementById("login");
  console.log("paso");
  login.addEventListener("submit", function (event) {
    event.preventDefault();
  });
}
function confirmarDatos() {
  Swal.fire({
    title: "usted a iniciado sesion correctamente",
    text: "por favor espere unos segundo",
    confirmButtonText: "listo",

    icon: "success"
  });
}

function ErrorDatosLogin() {
  swal.fire({
    title: "Datos invalidos",
    text: "Por favor registrarse",
    confirmButtonText: "listo",
    icon: "warning"
  })
}


