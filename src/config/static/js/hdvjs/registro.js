function guardaradmin(){
  const nameadmin = document.getElementById('nombreAdmin').value;
  const direccionadmin = document.getElementById('direccionAdmin').value;
  const teladmin = document.getElementById('telAdmin').value;
  const passadmin = document.getElementById('passAdmin').value;
  const emailadmin = document.getElementById('emailAdmin').value;
  const generoadmin= document.getElementById('generos').value;
  


  axios.post('guardar_admin',{
     fullname: nameadmin,
     telefono: teladmin,
     direccion: direccionadmin,
     email: emailadmin,
     password: passadmin,
     id_genero: generoadmin,
     
     
    },{
        headers:{
            'Content-Type': 'multipart/form-data'
        }
    }).then((res)=>{
        console.log(res.data)
     confirmarDatos()

    })
     .catch((error)=>{
        console.error(error)
        errorDatos()
       
    })
console.log(generoadmin)
}


function confirmarDatos() {
    Swal.fire({
        title: 'Usted ha sido correctamente registrado',
        text: 'estos datos han sido correctamente registrados',
        confirmButtonText: 'listo',
      backdrop: true,
        icon: 'success',
        timer: 5000

    })
};

function errorDatos(){
    swal.fire({
        title: 'Error en los datos',
        text: 'por favor rellenar los campos correctamente',
        confirmButtonText: 'listo',
        icon: 'error'


    }


    )
}

function prevenir() {
    const login = document.getElementById("log");
    console.log("paso")
    login.addEventListener("submit", function (event) {
        event.preventDefault();
    })
}