function guardar_cliente(){
    const name = document.getElementById('namecliente').value;
    const direccion = document.getElementById('direccioncliente').value;
    const telecliente = document.getElementById('telecliente').value;
    const tipodocumento = document.getElementById('documento').value;
    
    const generos = document.getElementById('generos').value;
   
    
    
    
    axios.post('guardar_cliente',{
        full_name:name, 
        tipo_document:tipodocumento,
        telefono:telecliente,
        direccion:direccion,
        id_genero:generos
      
        
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
  console.log(generos)
    }
    

    function guardar_pc(){
        
        const marcas = document.getElementById('marca').value;
        const series= document.getElementById('serie').value;
        const capacidad_ram = document.getElementById('ram').value;
        const tarjeta_gra = document.getElementById('tarjetagra').value;
        const disco = document.getElementById('discoduro').value;
        const procesador = document.getElementById('procesador').value;
        const sistema = document.getElementById('sistemaop').value;
        const fecha = document.getElementById('fecha').value;
       
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


function prevenir(){
const form = document.getElementById("formulario");
console.log("paso")
form.addEventListener("submit", function(event){
    event.preventDefault();
})}



