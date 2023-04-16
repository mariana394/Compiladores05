# ------------------------------------------------------------
# DATALOR: PARSER
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# PASER.... 
# ------------------------------------------------------------


#Grammar declaration

#<PROGRAM>
def p_program(p):
    '''program : PROGRAM ID SEMICOLON program_libraries program_vars program_function program_main END'''
    p[0] = "COMPILED"

#<LIBRERIES>
#Uso de las librerias en el programa  
  
def p_program_libraries(p):
    '''program_libraries : libraries
                         | empty'''

def p_libraries(p):
    '''libraries : full_library
                   | empty'''

def p_full_library(p):
    '''full_library : from_library import_library
                    | empty'''

def p_from_library(p):
    '''from_library : FROM ID
                    | empty'''

def p_import_library(p):
    '''import_library : IMPORT ID AS ID full_library'''   

#VARIABLES
#Uso de las variables en el programa
def p_vars(p):
    '''vars : VAR var_type  
            | empty'''

#<VAR CTE>
def p_var_cte(p):
    '''var_cte : ID 
             | CTE_INT 
             | CTE_FLOAT
             | CTE_CHAR'''

def p_s_type(p):
    '''s_type : INT 
              | FLOAT
              | CHAR'''

def p_c_type(p):
    '''s_type : FILE 
              | DATAFRAME
              | DATE'''
    
def p_var_type(p):
    '''var_type : var_c_type
               || var_s_type'''
    
def p_var_c_type(p):
    '''var_c_type : c_type ID var_c_type SEMICOLON var_type'''

def p_var_c_type2(p):
    '''var_c_type2 : COMMA ID var_c_type2
                   || empty'''
    
def p_var_s_type(p):
    '''var_s_type : s_type ID var_s_array var_s_type2 SEMICOLON var_type'''

def p_var_s_type2(p):
    '''var_s_type2 : COMMA ID var_s_array var_s_type2
                   | empty'''

def p_var_s_array(p):
    '''var_s_array : LSQBRAKET CTE_INT RSQBRAKET var_s_matrix
                   | empty'''

def p_var_s_matrix(p):
    '''var_s_matrix : LSQBRAKET CTE_INT RSQBRAKET
                    | empty'''

def p_variable(p):
    '''variable : ID variable_array
                | empty'''

def p_variable_array(p):
    '''variable_array : LSQBRAKET exp RSQBRAKET variable_matrix
                      | empty'''

def p_variable_matrix(p):
    '''variable_matrix : LSQBRAKET exp RSQBRAKET
                       | empty'''
    
#FUNCTIONS
#Uso de las funciones en el programa
def p_function(p):
    '''function : FUNCTION function_type ID LPAREN param RPAREN LBRAKET inner_body RETURN RBRAKET'''

def p_function_type(p):
    '''funtion_type : s_type
                    | VOID'''
    
#<PARAM>
def p_param(p):
    '''param : s_type ID param2'''

def p_param2(p):
    '''param2 : COMMA ID param2
              | empty'''

#<RETURN>
def p_return(p):
    '''return : RETURN VAR_CTE SEMICOLON'''

#Uso del main en el programa
def p_program_main(p):
    '''program_main : MAIN LBRAKE innerbody RBRAKET'''


#<BODY>
def p_body(p):
    '''body : LBRAKET inner_body RBRAKET'''

#<INNER_BODY>
def p_inner_body(p):
    '''inner_body : vars inner_body2'''

def p_inner_body2(p):
    '''inner_body2 : statement inner_body2
                   | empty'''

#<ASSIGN>
def p_assign(p):
    '''assign : variable ASSIGN exp SEMICOLON'''

#<CONDITION>
def p_condition(p):
    '''condtion : IF LPAREN exp RPAREN body condition2 SEMICOLON'''

def p_condition2(p):
    '''condtion2 : ELSE body
                 | empty'''
    
#<PRINT>
def p_print(p):
    '''print : PRINT LPAREN print_many RPAREN SEMICOLON'''

def p_print_many(p):
    '''print_many : print_type print_many2'''

def p_print_many2(p):
    '''print_many2 : COMMA print_many
                   | empty'''

def p_print_type(p):
    '''print_type : CTE_CHAR
                  || exp'''
    
#<READ>
def p_read(p):
    '''read : READ LPAREN variable RPAREN'''

#<CYCLE>
def p_cycle(p):
    '''cycle : FOR
             | WHILE'''
    
#<WHILE>
def p_while(p):
    '''while : DO body WHILE LPAREN exp RPAREN SEMICOLON'''

#<FOR>
def p_for(p):
    '''for : FOR LPAREN ID TO for_end RPAREN body SEMICOLON'''

def p_for_end(p):
    '''for_end : CTE_INT
               | ID'''
