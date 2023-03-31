# ------------------------------------------------------------
# DATALOR: LEXER 
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# Lexer.... 
# ------------------------------------------------------------

#IMPORTACION
import ply.lex as lex

#PALABRAS RESERVADAS
reserved = {
   #INICIO PROGRAMA
   'program' : 'PROGRAM',

   #LIBRERIAS
   'from' : 'FROM',
   'import' : 'IMPORT',
   'as' : 'AS',

   #CONDICIONALES
   'if' : 'IF',
   'else' : 'ELSE',

   #CYCLES
   'do': 'DO',
   'while' : 'WHILE',
   'for' : 'FOR',
   'to' : 'TO',
   
   #TIPO_VARIABLES
   'int' : 'INT',
   'float': 'FLOAT',
   'char' : 'CHAR',
   'timestamp' : 'TIMESTAMP',

    #DECLARACION DE VARIABLES
   'var':'VAR',

   #ESCRIBIR
   'print':'PRINT',

   #RETORNO
   'return' : 'RETURN',

   #FUNCIONES
   'function' : 'FUNCTION',
   'void' : 'VOID',

   #MAIN
   'main'  : 'MAIN',

   #TERMINAR EL PROGRAMA
   'end' :'END'
}
#List of tokens 
tokens = [
    'ID',

    #
    'LBRACKET', #{
    'RBRACKET', #}
    'LPAREN',
    'RPAREN',
    'RSQBRACKET', #]
    'LSQBRACKET',#[

    #EXPRESSIONS
    'EQUAL', #==
    'ASSIGN', #=
    'GTHAN',
    'LTHAN',
    'NOTEQUAL',
    'COLON',
    'SEMICOLON',
    'COMMA',
    
    
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_CHAR'

 ] + list(reserved.values())
