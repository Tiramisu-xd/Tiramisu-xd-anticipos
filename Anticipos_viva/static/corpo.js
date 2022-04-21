let fechaHoy= new Date().toISOString().substring(0,10);
let trmHoy = 0;
$.get("https://www.datos.gov.co/resource/ceyp-9c7c.json?vigenciadesde="+fechaHoy,function(ajaxresult){
    trmHoy=ajaxresult[0].valor;
});

let fecha_penHoy= new Date().toISOString().substring(0,10);
let trm_penHoy = 0;
$.get("https://v6.exchangerate-api.com/v6/8a4bd42bfbb115d4018a9e88/pair/PEN/COP"+fecha_penHoy,function(ajaxresult){
    trm_penHoy=ajaxresult[0].valor;
});

function preciosCiudades(){
    let cbxLugares = document.getElementById('cbxLugares');
    let Lugares = cbxLugares.value;

    document.getElementById('cbxLugaresSeleccionados').innerText = '${lugares}.';
}