/**
 * Operadores
 */

/**
 * Operadores de asignación
 */

// Operador de asignación

var x = 2;
var y = true;

// Operador de asignación de adición (+=)
var x = 2;
var y = 1;

x += y; // x = x + y
console.log(x);

// Operador de asignación de resta (-=)
var x = 1;
var y = 2;

x -= y; // x = x-y
console.log(x);

// Operador de asignación de multiplicación (*=)
var x = 5;
var y = 9;

x *= y; // x = x*y
console.log(x);

// Operador de asignacion de división (/=)
var x = 5;
var y = 9;

x /= y; // x= x/y
console.log(x);

// Operador de asignación de residuo (%=)
var x = 1;
var y = 4;

x %= y; //x = x % y
console.log(x);

// Operador de asignación de exponenciación (**=)
var x = 5;
var y = 3;

x **= y; //x = x ** y
console.log(x);

/**
 * Operadores de comparación
 */

// Operador igual (==)
console.log(3 == 3);
console.log(3 =='3');

// Operador no es igual (!=)
console.log(3!=3);
console.log(3 !='3');

// Operador estrictamente igual (===)
console.log(3===3);
console.log(3==='3');

// Operador de desigualdad estricta (!==)
console.log(3!=='3');

// Operadores >, >=, <, <=
console.log(3 > 4);
console.log(3 >= 3);
console.log(2 < 4);
console.log(2 <= 2);

/**
 * Operadores Aritmeticos
 * 
 * +, -, , /, %, **
 */
console.log(2+2);
console.log(2-2);
console.log(2*2);
console.log(2/2);
console.log(2%2);
console.log(2**2);

// Operador de incremento (++)
var numero = 0;
console.log(++numero);

var numero_2 = 0;
console.log(numero_2++);
console.log(numero_2);

// Operador de decremento
var numero_3 = 3;
console.log(--numero_3);

var numero_4 = 3;
console.log(numero_4--);
console.log(numero_4);

/**
 * Operadores logicos
 */
// Operador AND (&&)

console.log(true && true);
console.log(2>3 && 1<=2);

// Operador OR (││) 
console.log(true || false);

// Operador NOT (!)
console.log(!true);
console.log(!false);

// Operador de cadena o concatenacion (+)
var nombre = "Jym";
var apellido = "Lara";
var nombreCompleto = nombre + " " + apellido;
console.log(nombreCompleto);

// Operador condicional (condicion ? val1 : val2)
console.log(2>3 ? "Es mayor" : "Es menor");

// Operador de desstructuración
var persona = {
    nombre: "Jym",
    apellido: "Lara"
}

var {nombre} = persona;
console.log(nombre);
console.log(persona);

var {nombre, apellido} = persona;
console.log(nombre);
console.log(apellido);

var {nombre:xyz, apellido:abc} = persona;
console.log(xyz);
console.log(abc);

// desestructuracion de arreglos
var arreglo = [1,2,3,4,5,6,7,8,9,0];

var [primeraPosicion, dos] = arreglo;
console.log(primeraPosicion);
console.log(dos);

/**
 * Operador de miembro o acceso de propiedad
 */
// Notación punto
var persona = {
    nombre: "Jym",
    apellido: "Lara"
}
console.log(persona.nombre);
console.log(persona.apellido);

// notacion por corchetes
var persona = {
    nombre: "Jym",
    apellido: "Lara"
}
console.log(persona['nombre']);

var arreglo = [1,2,3,4,5,6,7,8,9,0];
console.log(arreglo[3]);

// Operacion de determinacion de tipo (typeof)
console.log(typeof 'Jym');
console.log(typeof 285);
console.log(typeof true);