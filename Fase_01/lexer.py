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

   #TIPOS_VARIABLES_COMPUESTA 
   'dataframe' : 'DATAFRAME',
    'date' : 'DATE',

    #DECLARACION DE VARIABLES
   'var':'VAR',

   #ESCRIBIR
   'print':'PRINT',

   #LEER
    'read':'READ',

   #RETORNO
   'return' : 'RETURN',

   #FUNCIONES
   'function' : 'FUNCTION',
   'void' : 'VOID',

   #MAIN
   'main'  : 'MAIN',

   #TERMINAR EL PROGRAMA
   'end' :'END',

   #FUNCIONES ESPECIALES
   'exploration' : 'EXPLORATION',
   'financial_state' : 'FINANCIAL_STATE',
   'season_analyzer' : 'SEASON_ANALYSIS',
   'trend_prediction' : 'TREND_PREDICTION',
   'dummi_regression' : 'DUMMI_REGRESSION',
   
   #FUNCIONES ESPECIALES NICE TO HAVE
   'model_predict' : 'MODEL_PREDICT'
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
    'NOTEQUAL', #!=
    'COLON',
    'SEMICOLON',
    'COMMA',
    'OR',
    'AND',
    
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    
    #CONSTANTES
    'CTE_INT',
    'CTE_FLOAT',
    'CTE_CHAR'

 ] + list(reserved.values())

# Regular expression rules for simple tokens
t_LBRACKET    = r'\{'
t_RBRACKET    = r'\}'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_RSQBRACKET = r'\]'
t_LSQBRACKET = r'\['
t_EQUAL = r'=='
t_ASSIGN = r'='
t_GTHAN = r'>'
t_LTHAN = r'<'
t_NOTEQUAL = r'!='
t_COLON = r':'
t_SEMICOLON = r';'
t_COMMA = r','
t_OR = r'\|\|'
t_AND = r'&&'
t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'

#CONSTANTES
def t_CTE_INT(t):
    r'\d+'
    t.value = int(t.value)    
    return t

def t_CTE_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)    
    return t

def t_CTE_CHAR(t):
    r'\'[a-zA-Z0-9]*\''
    t.value = str(t.value)    
    return t

#ID
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value,'ID')   
    return t

# Ignorar tabs
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Construir el lexer
lexer = lex.lex()

# Prueba de entrada

#data = 
'''
program TESTCORRECTO;

import pandas as pd
import numpy as np
import csv 

var
dataframe costos, ventas;
date inicio, fin;

function void message (char name, int size){
	print ("Se ha leido el dataframe ", name, " con un tamano de ", size);
}

main {
costos = read csvcostos;
ventas = read csvventas;
inicio = '10011999';
fin = '10012023';

print(financial_state(ventas, costos,inicio, fin))

}
end
'''

#Pasar la entrada
#lexer.input(data)

#Tokenize
#while True:
#    tok = lexer.token()
#    if not tok: 
#        break      # Terminar lectura
#    print(tok)
