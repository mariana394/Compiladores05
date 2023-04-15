#Grammar declaration
def p_program(p):
    '''program : PROGRAM ID SEMICOLON program_libraries program_vars program_function program_main END'''
    p[0] = "COMPILED"

#Uso de las librerias en el programa    
def p_program_libraries(p):
    '''program_libraries : libraries
                         | empty'''

#Uso de las variables en el programa
def p_program_vars(p):
    '''program_vars : vars  
                    | empty'''

#Uso de las funciones en el programa
def p_program_function(p):
    '''program_function : function
                        | empty'''

#Uso del main en el programa
def p_program_main(p):
    '''program_main : MAIN LBRACE innerbody RBRACE'''


