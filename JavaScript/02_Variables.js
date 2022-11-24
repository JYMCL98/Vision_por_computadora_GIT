/**
 * Variables
 * 
 * 3 Formas de definir variables
 * 
 * 1.- var
 * 2.- let
 * 3.- const
 * 
 */

// Variables con var
var nombre = 'Jym';
console.log(nombre);

var edad = 27;
console.log(edad);

var persona = {
    nombre: 'Jym',
    apellido: 'Lara',
    edad:23,
    direccion: {
        calle: 'Chapultepec',
        numeroDeCasa: 25
    },
    ciudades: [
        'Orizaba',
        'Texcoco',
        'Berlin'
    ]
}
console.log(persona);

var ciudad;
ciudad = 'Orizaba';
ciudad = 'Texcoco';
ciudad = 25;
console.log(ciudad);

// Variables con let
let nombre = 'Jym';
console.log(nombre);

/**
 * Sirve para declarar variables de forma local
 * puede ser en un bloque de código.
 * Y si se ocupa var si se puede definir de forma global.
 */
{
    let saludo = 'Hola mundo';
    console.log(saludo);
}

/**
 * Variable con const
 * Generalmente el nombre de la variable se escribe en 
 * mayusculas y si existen espacios son representados
 * con un guión bajo.
 * No se puede dejar como indefinido, es decir no puede
 * cambiar a lo largo del código.
 */
const PI = 3.1416;
console.log(PI);

var nombre = 'Jym';
var saludo = `Hola soy ${nombre}`;
console.log(saludo);

