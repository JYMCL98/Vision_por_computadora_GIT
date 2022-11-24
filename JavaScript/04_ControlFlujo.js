/**
 * Control de flujo
 */

// Estructura IF
// if(condición){

//}

var llueve = false;
if (llueve) {
    console.log("Necesito una sombrilla");
}

var administrador = true;
if (administrador) {
    console.log("Bienvenido al sistema");
}

var administrador = "administrador";
if (administrador === "administrador") {
    console.log("Bienvenido al sistema");
}

const MAYORIA_DE_EDAD = 18;
var edadPersona = 18;
if (edadPersona >= MAYORIA_DE_EDAD) {
    console.log("Es mayor de edad");
} else {
    console.log("No es mayor de edad");
}

var semaforo = "azul";
if (semaforo === "verde") {
    console.log("Arranca");
} else if(semaforo==="amarillo"){
    console.log("Listo?");
} else if (semaforo==="rojo"){
    console.log("Motores apagados");
} else{
    console.log("Color no valido");
}

// Estructura switch
var producto = "naranja";
switch (producto) {
    case "papaya":
        // codigo
        console.log("Las papayas cuestan 30 el Kg");
        break;
    
    case "naranja":
        // codigo
        console.log("Las naranjas cuestan 15 el Kg");
        break;
    
    case "mango":
        // codigo
        console.log("El mango cuesta 32 el Kg");

    default:
        console.log("No se conoce el precio");
        break;
}