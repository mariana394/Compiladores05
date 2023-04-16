![This is an image](/Assets/logo.png)
# Compiladores05
## Alumnos: Mario Juarez A01411049 Mariana Favarony A01704671
## Diagramas de Sintaxis: https://drive.google.com/file/d/1rT--1iBT-UHtPp6fK2LWhKtAkdhpEeFS/view?usp=sharing


## Bugs de versión
 ### version 2.2.0
 <br>Read - No se puede asignar y por ende no tiene punto y coma
 <br>Char - No funciona con espacios en blanco
 <br>* Revisar flujo de "exp" en el parser porque no se llega a ID
 <br>Print -  Debido al flujo erroneo print no permite exp y se forzo a aceptar ID
 <br>Asignacion - No se pueden asignar funciones a una variable
 <br>* Se mantienen 2 conflicts shift/reduce en el parser
 <br>Colon - Se han declarado, pero no se estan usando

 ### version 2.3.0
 <br>call_function - Al llamar una funcion void sin asignar a nada esta se llama sin finalizar con punto y coma
<br> * Se mantienen 2 conflicts shift/reduce en el parser


## Correcciones de diseño
 ### version 2.3.0
 <br>return - Se cambio el parametro de return de var_cte a exp
 <br>inner_body - Fue modificado para evitar que se dentro de condicional y  ciclo se declaren    variables  dejando así que las variables sean unicamente declaradas dentro de la funcion y main 
 <br>assign - Ya es posible asignar read y funciones especiales a una variable
