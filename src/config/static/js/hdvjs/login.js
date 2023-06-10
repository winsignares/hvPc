

// Función para validar el correo y la contraseña
 function validarlogin() {
    const nameuser= document.getElementById("emailuser").value;
    const passuser= document.getElementById("passuser").value;
    
    console.log("getData.Email:'",nameuser,"'.and.Password:'",passuser,"'")
  
    axios.post('validarlogin', {
    email: nameuser,
    password: passuser
    })
    .then(function(res){        
      console.log(res.data);
      confirmarDatos()
      window.location.href = res.data

  })
  .catch((err) => {
      console.log(err);
  })
}
function prevenir() {
    const login = document.getElementById("login");
    console.log("paso")
    login.addEventListener("submit", function (event) {
        event.preventDefault();
    })
}
function confirmarDatos() {
  Swal.fire({
      title: 'usted a iniciado sesion correctamente',
      text: 'disfrute de nuestro sistema',
      confirmButtonText: 'listo',
    
      icon: 'success'

  })
};