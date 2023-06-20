// Función para validar el correo y la contraseña
function validarlogin() {
  const nameuser = document.getElementById("emailuser").value;
  const passuser = document.getElementById("passuser").value;

<<<<<<< HEAD
  })
  .catch((err) => {
      console.log(err);
      errorDatos()
  })
=======
  console.log("getData.Email:'", nameuser, "'.and.Password:'", passuser, "'");

  axios
    .post("validarlogin", {
      email: nameuser,
      password: passuser
      
    }).then(function (res) {
        confirmarDatos()
        console.log(res.data)
        setTimeout(function(){

        window.location.href = res.data
        },4000 )
        
    })
    .catch((err) => {
        console.log(err)
        ErrorDatosLogin()
    })
>>>>>>> 2d931d41f23045f1d78e263b390b38fb6c573e2c
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
<<<<<<< HEAD
};
function errorDatos(){
    swal.fire({
        title: 'lo sentimos, su informacion es incorrecta',
        text: 'por favor registrarse',
        confirmButtonText: 'listo',
        icon: 'warning'


    }


    )
}
=======
}
>>>>>>> 2d931d41f23045f1d78e263b390b38fb6c573e2c
