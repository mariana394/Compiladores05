![This is an image](/Assets/logo.png)
# Compiladores05
## Alumnos: Mariana Favarony A01704671 Mario Juarez A01411049
## Diagramas de Sintaxis: https://drive.google.com/file/d/1rT--1iBT-UHtPp6fK2LWhKtAkdhpEeFS/view?usp=sharing


### Descripción general del avance
<br> **STATUS: ** "JALA avance 7"
<br> Tabla de funciones y de variables creada y funcional
<br> Cubo semantico creado
<br> Creacion de cuadruplos para estatutos lineales, secuenciales
<br> Elementos no-atomicos homogeneos
<br> Mapa de memoria
<br> Maquina virtual: estatutos lineales, cuadrulos: lineales, IF-Else, For, do-while, arreglos y matrices

<br>La version 3.5.6 de DATALOR presenta el lexer y el parser con la debida sintaxis y reglas gramaticas. Se realizaron pruebas para revisar el funcionamiento correcto, se realizaron correcciones y siguen pendientes algunos errores y observaciones a corregir mencionadas a continuacion:


## Bugs de versión
### version 3.5.3
<br> Se mantienen warnings de las versiones anterioes 

<br> A las variables locales aun no se les asigna espacio en memoria 
<br> Pendiente: verificacion de la declaracion de varibles

### version 3.4.0
<br> Se mantienen los errores de la version 2.3.0
 
 ### version 2.3.0
 <br>call_function - Al llamar una funcion void sin asignar a nada esta se llama sin finalizar con punto y coma. El punto y coma solo existe en asignacion 
<br> * Se mantienen 2 conflicts shift/reduce en el parser (WARNINGS)
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
