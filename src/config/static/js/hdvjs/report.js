function guardar_cliente(){
    const name = document.getElementById('namecliente').value;
    const direccion = document.getElementById('direccioncliente').value;
    const telecliente = document.getElementById('telecliente').value;
    const tipodocumneto = document.getElementById('cedula').value;
    const men = document.getElementById('men').value;
    const woman = document.getElementById('woman').value;
    const tarjeta = document.getElementById('tarjeta').value;

    axios.post('guardar_cliente',{
        full_name:name,
        tipo_document:tipodocumneto,
        tipo_document:tarjeta,
        telefono:telecliente,
        direccion:direccion,
        id_genero:men,
        id_genero:woman
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
console.log(tipodocumneto)
    }
    

    function guardar_pc(){
        var boton =document.getElementById('ok')
        const marcas = document.getElementById('marca').value;
        const series= document.getElementById('serie').value;
        const capacidad_ram = document.getElementById('ram').value;
        const tarjeta_gra = document.getElementById('tarjetagra').value;
        const disco = document.getElementById('discoduro').value;
        const procesador = document.getElementById('procesador').value;
        const sistema = document.getElementById('sistemaop').value;
        const fecha = document.getElementById('fecha').value;
        boton.addEventListener('click', function(event) {
            event.preventDefault();
            // Realiza tus acciones o muestra tus contenidos sin que la página se actualice
            console.log('Haz clic en el enlace sin actualizar la página');
          });
        axios.post('guardar_pcs',{
            marca:marcas,
            serie:series,
            capacidad_Ram:capacidad_ram,
            tarjeta_grafica:tarjeta_gra,
            capacidad_discoDuro:disco,
            procesador:procesador,
            sistema_operativo:sistema,
            fecha_adquisicion:fecha
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
    console.log(fecha)
        }



