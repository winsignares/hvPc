function guardaradmin(){
  const nameadmin = document.getElementById('nombreAdmin').value;
  const direccionadmin = document.getElementById('direccionAdmin').value;
  const teladmin = document.getElementById('telAdmin').value;
  const passadmin = document.getElementById('passAdmin').value;
  const emailadmin = document.getElementById('emailAdmin').value;
  const generoadmin= document.getElementById('generoAdmin').value;
  const genero_admin= document.getElementById('generoAdmins').value;


  axios.post('guardar_admin',{
     fullname: nameadmin,
     telefono: teladmin,
     direccion: direccionadmin,
     email: emailadmin,
     password: passadmin,
     id_genero: generoadmin,
     id_genero: genero_admin
     
    },{
        headers:{
            'Content-Type': 'multipart/form-data'
        }
    }).then((res)=>{
        console.log(res.data)
        alert("success")
    })
     .catch((error)=>{
        console.error(error)
        alert("no")
    })
console.log(generoadmin)
}


function DatoSeguro() {
    Swal.fire({
        title: 'Deseas Guardar este dato',
        text: 'Recuerda que este dato será almacenado',
        confirmButtonText: 'confirmar',
        showCancelButton: true,
        icon: 'warning'

    })
};

