![This is an image](/Assets/logo.png)
# Compiladores05
## Alumnos: Mariana Favarony A01704671 Mario Juarez A01411049
## Diagramas de Sintaxis: https://drive.google.com/file/d/1rT--1iBT-UHtPp6fK2LWhKtAkdhpEeFS/view?usp=sharing


### Descripción general del avance
<br> **STATUS: ** "Jala con errores"
<br>Se encuentra el cubo semantico de manera textual dentro del documento de documentacion
<br>La version 3.4.0 de DATALOR presenta el lexer y el parser con la debida sintaxis y reglas gramaticas. Se realizaron pruebas para revisar el funcionamiento correcto, se realizaron correcciones y siguen pendientes algunos errores y observaciones a corregir mencionadas a continuacion:
Z

## Bugs de versión

### version 3.4.0
<br> Se mantienen los errores de la version 2.3.0

 ### version 2.3.0
 <br>call_function - Al llamar una funcion void sin asignar a nada esta se llama sin finalizar con punto y coma. El punto y coma solo existe en asignacion 
<br> * Se mantienen 2 conflicts shift/reduce en el parser
<br> function -> La funcion no estaba ciclada en la parte inicial del programa lo que nos mandaba a que solo se pudiera definir una funcion. Adicionalmente no acepta funciones sin parametros (esta bien)
 <br>Char - No funciona con espacios en blanco
<br>Colon - Se han declarado, pero no se estan usando


 ### version 2.2.0
 <br>Read - No se puede asignar y por ende no tiene punto y coma
 <br>Char - No funciona con espacios en blanco
 <br>* Revisar flujo de "exp" en el parser porque no se llega a ID
 <br>Print -  Debido al flujo erroneo print no permite exp y se forzo a aceptar ID
 <br>Asignacion - No se pueden asignar funciones a una variable
 <br>* Se mantienen 2 conflicts shift/reduce en el parser
 <br>Colon - Se han declarado, pero no se estan usando



## Correcciones de diseño
 ### version 3.4.0
 <br> function - Se modifico para que lograra tener 0 o mas funciones
 <br> validacion correcta for (parametros, body, no acepta funciones como parametro)
 <br> Se agregaron al lexer tokens faltantes
 
 ### version 2.3.0
 <br>return - Se cambio el parametro de return de var_cte a exp
 <br>inner_body - Fue modificado para evitar que se dentro de condicional y  ciclo se declaren    variables  dejando así que las variables sean unicamente declaradas dentro de la funcion y main 
 <br>assign - Ya es posible asignar read y funciones especiales a una variable

 ## Por revisar...
 <br> * Integracion de tipo boolean
 <br> * Comentarios con python o propios del lenguaje
