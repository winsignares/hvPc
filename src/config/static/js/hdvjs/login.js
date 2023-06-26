// Función para validar el correo y la contraseña
function validarlogin() {
  const nameuser = document.getElementById("emailuser").value;
  const passuser = document.getElementById("passuser").value;

  console.log("getData.Email:'", nameuser, "'.and.Password:'", passuser, "'");

  axios
    .post("validarlogin", {
      email: nameuser,
      password: passuser
      
    }).then(function (res) {
      console.log(res.data)
        confirmarDatos()
        
        setTimeout(function(){
          data = res.data  
          window.location.href = res.data.href
        window.location.href = res.data
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


