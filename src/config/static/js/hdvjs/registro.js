function guardaradmin(){
  const nameadmin = document.getElementById('nombreAdmin');
  //const teladmin = document.getElementById('telAdmin');
  //const passadmin = document.getElementById('passAdmin');
  //const emailadmin = document.getElementById('emailAdmin');
  //const menadmin = document.getElementById('men');
  //const womanadmin = document.getElementById('woman');

 axios.post('/guardaradmin',{
     fullname:nameadmin.value,
     //email: emailadmin.value,
     //telefono: teladmin.value,
     //password: passadmin.value,
     ///men: menadmin.value,
     //woman: womanadmin.value
    },
    {
    headers: {
        'Content-Type': 'multipart/form-data'

        }
    }
    ).then((res) => {
        console.log(res.data)
        alert('funciona')
    })
    .catch((error) => {
        console.error(error)
        alert('no')
    })





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