![This is an image](/Assets/logo.png)
# Compiladores05
## Alumnos: Mario Juarez A01411049 Mariana Favarony A01704671
## Diagramas de Sintaxis: https://drive.google.com/file/d/1rT--1iBT-UHtPp6fK2LWhKtAkdhpEeFS/view?usp=sharing


##Bugs de versión
 ###version 2.2.0
 Read - No se puede asignar y por ende no tiene punto y coma
 Char - No funciona con espacios en blanco
 * Revisar flujo de "exp" en el parser porque no se llega a ID
 Print -  Debido al flujo erroneo print no permite exp y se forzo a aceptar ID
 Asignacion - No se pueden asignar funciones a una variable
 * Se mantienen 2 conflicts shift/reduce en el parser