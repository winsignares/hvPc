
function guardar_cliente() {
    const name = document.getElementById('namecliente').value;
    const direccion = document.getElementById('direccioncliente').value;
    const telecliente = document.getElementById('telecliente').value;
    const tipodocumento = document.getElementById('documento').value;

    const generos = document.getElementById('generos').value;




    axios.post('guardar_cliente', {
        full_name: name,
        tipo_document: tipodocumento,
        telefono: telecliente,
        direccion: direccion,
        id_genero: generos


    }, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then((res) => {
        console.log(res.data)
        alert("success")
    })
        .catch((error) => {
            console.error(error)
            alert("no")
        })
    console.log(generos)
}


function guardar_pc() {

    const marcas = document.getElementById('marca').value;
    const series = document.getElementById('serie').value;
    const capacidad_ram = document.getElementById('ram').value;
    const tarjeta_gra = document.getElementById('tarjetagra').value;
    const disco = document.getElementById('discoduro').value;
    const procesador = document.getElementById('procesador').value;
    const sistema = document.getElementById('sistemaop').value;
    const fecha = document.getElementById('fecha').value;

    axios.post('guardar_pcs', {
        marca: marcas,
        serie: series,
        capacidad_Ram: capacidad_ram,
        tarjeta_grafica: tarjeta_gra,
        capacidad_discoDuro: disco,
        procesador: procesador,
        sistema_operativo: sistema,
        fecha_adquisicion: fecha
    }, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then((res) => {
        console.log(res.data)
        alert("success")
    })
        .catch((error) => {
            console.error(error)
            alert("no")
        })
    console.log(fecha)
}


function guardar_reportes() {

    const clientes = document.getElementById('clientes').value;
    const pcs = document.getElementById('pcs').value;
    const admin = document.getElementById('admin').value;
    const programas = document.getElementById('programas').value;
    const observaciones = document.getElementById('observaciones').value;
    const estado = document.getElementById('estado').value;
    const fecha_ini = document.getElementById('fechaini').value;
    const fecha_fin = document.getElementById('fechaend').value;

    axios.post('guardar_reports', {
        id_cliente: clientes,
        id_pc: pcs,
        id_admin: admin,
        programas_install: programas,
        observaciones: observaciones,
        estado: estado,
        fecha_inicio: fecha_ini,
        fecha_fin: fecha_fin
    }, {
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    }).then((res) => {
        console.log(res.data)
        alert("success")
    })
        .catch((error) => {
            console.error(error)
            alert("no")
        })
    console.log(fecha_fin)
}


function prevenir() {
    const form = document.getElementById("formulario");
    console.log("paso")
    form.addEventListener("submit", function (event) {
        event.preventDefault();
    })
}


function limpiarcliente() {
    var name = document.getElementById('namecliente');
    var direccion = document.getElementById('direccioncliente');
    var telecliente = document.getElementById('telecliente');
    var tipodocumento = document.getElementById('documento');
    var generos = document.getElementById('generos');
    console.log("paso")

    name.value = ""
    direccion.value = ""
    telecliente.value = ""
    tipodocumento.value = ""
    generos.value = ""


}

function limpiarpc() {
    const marcas = document.getElementById('marca');
    const series = document.getElementById('serie');
    const capacidad_ram = document.getElementById('ram');
    const tarjeta_gra = document.getElementById('tarjetagra');
    const disco = document.getElementById('discoduro');
    const procesador = document.getElementById('procesador');
    const sistema = document.getElementById('sistemaop');
    const fecha = document.getElementById('fecha');
    console.log("paso")

    marcas.value = ""
    series.value = ""
    capacidad_ram.value = ""
    tarjeta_gra.value = ""
    disco.value = ""
    procesador.value = ""
    sistema.value = ""
    fecha.value = ""


}


function limpiarReportes() {
    const clientes = document.getElementById('clientes');
    const pcs = document.getElementById('pcs');
    const admin = document.getElementById('admin');
    const programas = document.getElementById('programas');
    const observaciones = document.getElementById('observaciones');
    const estado = document.getElementById('estado');
    const fecha_ini = document.getElementById('fechaini');
    const fecha_fin = document.getElementById('fechaend');
    console.log("paso")

    clientes.value = ""
    pcs.value = ""
    admin.value = ""
    programas.value = ""
    observaciones.value = ""
    estado.value = ""
    fecha_ini.value = ""
    fecha_fin.value = ""


}
function mostrarImagen(event){
var imagenSource= event.target.result;
var previewImage= document.getElementById('preview');
previewImage.src = imagenSource;

}
function procesarArchivo(event){
var imagen= event.target.files[0];
var lector = new FileReader();
lector.addEventListener('load', mostrarImagen, false)
lector.readAsDataURL(imagen);


}

document.getElementById("archivo")
 .addEventListener('change', procesarArchivo, false);



function buscarAdmin(){

    const inputadmin= document.getElementById("admin")
    axios.get("obtenerNombre",{
        "full_name": inputadmin.value

    }
    ).then((res) => {
        console.log(res.data)
        alert("success")
    })
}