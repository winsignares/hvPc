

// Función para validar el correo y la contraseña
 function validarlogin() {
    const nameuser= document.getElementById("emailuser").value;
    const passuser= document.getElementById("passuser").value;
    
    console.log("getData.Email:'",nameuser,"'.and.Password:'",passuser,"'")
  
    axios.post('validarlogin', {
    email: nameuser,
    password: passuser
    })
    .then(response=>{
      console.log(response.data);
      alert("success")
     window.location.href='indexhome';
     return true;
    
     
    })
    .catch(error =>{
    console.error(error)
    alert("no")
  
    return false;
  
    });

    
  }
