# ------------------------------------------------------------
# DATALOR: PARSER
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# PASER.... 
# ------------------------------------------------------------
import ply.yacc as yacc
from lexer import tokens
import sys
from func_var_tables import DirFunc
from quadruples import Quadruples
from dictionary import Dictionary

#Global variables
curr_type = ''
scope = 0 
curr_name = ''
curr_function = ''
# GB for arrays and Matrix
curr_rows = 0
curr_columns = 0
curr_dim = 0 #por si las moscas
curr_temp = 0
g_test = 10

#Objects
tables = DirFunc()
quad = Quadruples()
oracle = Dictionary()
#<PROGRAM>
def p_program(p):
    '''program : PROGRAM ID SEMICOLON program_libraries program_vars program_function program_main end'''
    p[0] = "COMPILED"

def p_end(p):
    '''end : END empty'''
    tables.print()
#EMPTY
def p_empty(p):
    'empty : '
    pass

#__________________GENERIC NEURALGIC POINTS__________________#

#Neuralgic Point for saving the ID and passing it to the corresponding table
def p_id_saver(p):
    '''id_saver : ID empty '''
    global curr_name
    curr_name = p[1]
    #print(curr_name)

#Neuralgic point for constant Int, helps us to save the constant in the constants table and memory no matter where the constant is in the code. 
# cte_int -> for (top of the cycle), array/matrix dimensions, special functions
def p_int_const_saver(p):
    '''int_const_saver : CTE_INT empty'''
    tables.add_const(p[1], type (p[1]))

#Neuralgic point number 1 for all expressions where we check first if we have a pending operator
def p_release_exp(p):
    '''release_exp : empty'''
    global g_test
    print ("Tipo de Operacion", g_test)
    quad.create_exp_quadruple(g_test)

#_________________________<LIBRERIES>_____________________________#
#Uso de las librerias en el programa  
  
def p_program_libraries(p):
    '''program_libraries : from_library import_library 
                         | empty'''

def p_from_library(p):
    '''from_library : FROM ID
                    | empty'''

def p_import_library(p):
    '''import_library : IMPORT ID AS ID  program_libraries'''   

#__________________________VARIABLES____________________
#Uso de las variables en el programa
def p_var_type(p):
    '''var_type : var_c_type
                | var_s_type'''

def p_program_vars(p):
    '''program_vars : VAR var_type  
                    | empty'''

#<VAR CTE>
# def p_var_cte(p):
#     '''var_cte : ID 
#              | CTE_INT 
#              | CTE_FLOAT
#              | CTE_CHAR'''

def p_s_type(p):
    '''s_type : INT 
              | FLOAT
              | CHAR'''
    #NEURALGIC POINTS
    global curr_type 
    curr_type = p[1]
    #print(curr_type)

def p_c_type(p):
    '''c_type : DATAFRAME
              | DATE'''
    #NEURALGIC POINTS
    global curr_type 
    curr_type = p[1]
    #print(curr_type)

def p_var_multiple(p):
    '''var_multiple : var_type
                    | empty'''

def p_var_c_type(p):
    '''var_c_type : c_type id_saver add_c_var var_c_type2 SEMICOLON var_multiple'''

def p_var_c_type2(p):
    '''var_c_type2 : COMMA id_saver add_c_var var_c_type2
                   | empty'''
    
def p_add_c_var(p):
    '''add_c_var : empty'''
    global curr_type, curr_name, scope
    tables.add_vars(curr_name,scope,curr_type)
    
#------Será necesario saber el tamaño de las variables tipo array??------#
def p_var_s_type(p):
    '''var_s_type : s_type id_saver var_s_array add_s_var var_s_type2 SEMICOLON var_multiple'''

def p_var_s_type2(p):
    '''var_s_type2 : COMMA id_saver var_s_array add_s_var var_s_type2
                   | empty'''

#____NEURALGIC POINT______#
def p_add_s_var(p):
    '''add_s_var : empty'''
    global curr_type, curr_name, scope, curr_columns, curr_rows
    tables.add_vars(curr_name,scope,curr_type, curr_rows, curr_columns)
    #RESET variables to 0 for the next one to be read
    curr_columns = 0
    curr_rows = 0
#----var_s_dimensions era anteriormente CTE_INT y funcionaba bien-----#
def p_var_s_array(p):
    '''var_s_array : LSQBRACKET var_s_dimesions RSQBRACKET var_s_matrix 
                   | empty'''

def p_var_s_matrix(p):
    '''var_s_matrix : LSQBRACKET var_s_dimesions RSQBRACKET
                    | empty'''

#____NEURALGIC POINT______#
def p_var_s_dimesions(p):
    '''var_s_dimesions : CTE_INT empty'''
    global curr_rows, curr_columns, curr_dim
    #____Classifying s_type variables____#
    #Add the size as a constant in the constants variable
    tables.add_const(p[1], type (p[1]))
    #MATRIX
    if (curr_rows != 0):
        if (curr_columns == 0):
            curr_columns = p[1]
            tables.check_stype_size(curr_columns)
    #ARRAY        
    else:
        curr_rows = p[1]
        tables.check_stype_size(curr_rows)  


def p_variable(p):
    '''variable : id_saver variable_array'''
    global curr_name, scope
    type = tables.search_variable_existance(curr_name, scope)
    quad.type_stack_push(type)
    quad.operands_stack_push(curr_name)

    #print(scope, ' factor variable ', curr_name, type )

def p_variable_array(p):
    '''variable_array : LSQBRACKET exp RSQBRACKET variable_matrix
                      | empty'''

def p_variable_matrix(p):
    '''variable_matrix : LSQBRACKET exp RSQBRACKET
                       | empty'''
    
#_________________________________________FUNCTIONS______________________________________#
#
#Program functions 
def p_program_function(p):
    '''program_function : FUNCTION f_type id_saver func_creator LPAREN param RPAREN LBRACKET program_vars inner_body return RBRACKET program_function
                        | empty'''


#type of funtion return
def p_f_type(p):
    '''f_type : INT 
              | FLOAT
              | CHAR
              | VOID'''
    global curr_type,scope
    curr_type = p[1]
    scope += 1
    #print(curr_type,scope)
#______FUNCTION___NEURALGIC POINTS________#

def p_func_creator(p):
    '''func_creator : empty'''
    global scope, curr_function, curr_type, curr_name
    curr_function = curr_name
    tables.add_function(curr_name,scope,curr_type)
#_____________________________________________________

#<PARAM>
def p_param(p):
    '''param : s_type id_saver add_params param2'''
    
def p_param2(p):
    '''param2 : COMMA s_type id_saver add_params param2
              | empty'''

#________PARAMS NEURALGIC POINTS___________________________
def p_add_params(p):
    '''add_params : empty'''
    global curr_type, curr_name, scope, curr_function
    tables.add_vars(curr_name,scope,curr_type)
    tables.add_params(curr_function,curr_type)

#<RETURN>
def p_return(p):
    '''return : RETURN exp SEMICOLON
              | empty'''
#____________________MAIN_________________#
#Uso del main en el programa
def p_program_main(p):
    '''program_main : MAIN main_id LBRACKET program_vars inner_body RBRACKET'''

def p_main_id(p):
    '''main_id : empty'''
    global scope
    scope += 1
    tables.add_function('main',scope,'void')
    
#<BODY>
def p_body(p):
    '''body : LBRACKET inner_body RBRACKET'''

#<INNER_BODY>
def p_inner_body(p):
    '''inner_body :  statement inner_body
                  | empty'''


#__________________________<ASSIGN>____________________________________
def p_assign(p):
    '''assign : variable keep_assign specialf_assign end_assign'''
    quad.print_poperands()

def p_specialf_assign(p):
    '''specialf_assign : exp
                       | special_function
                       | read'''
    
#keep the assign -> STACK
def p_keep_assign(p):
    '''keep_assign : ASSIGN empty'''
   # print('ASSIGN ', p[1])
    global curr_name, scope
    #PUSH operators and operanas to the stakc
    #quad.operands_stack_push(curr_name)
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
    #save the type 
    # var_type = tables.search_variable_existance(curr_name, scope)
    # quad.type_stack_push(var_type)

   
    #quad.type_stack_push(curr_type)


#END-> Quadruple
def p_end_assign(p):
    '''end_assign : SEMICOLON empty'''
    quad.assign_quadruple()

#_________________________<CONDITION>___________________________________
def p_condition(p):
    '''condition : IF LPAREN exp RPAREN condition_GOTOF body condition2 SEMICOLON end_condition'''

def p_condition2(p):
    '''condition2 : ELSE condition_GOTO body
                 | empty'''
    
def p_condition_GOTO(p):   
    '''condition_GOTO : empty'''
    print('\t\tcondition_GOTO\n')
    quad.insert_goto(17)

def p_end_condition(p):
    '''end_condition : empty'''
    jump = quad.jump_stack_pop()
    where = quad.cont_place()
    quad.fill(jump, where)

# Neuralgic point
def p_condition_GOTOF(p):   
    '''condition_GOTOF : empty'''
    print('\t\tcondition_GOTOF\n')
    quad.jump_stack_push()
    quad.insert_goto(19)

    
#<PRINT>
def p_print(p):
    '''print : PRINT LPAREN print_many RPAREN SEMICOLON'''
    
#Notas modificar print para que sirva con exp en ID
def p_print_type(p):
    '''print_type : exp'''

def p_print_many(p):
    '''print_many : print_type print_many2 '''

def p_print_many2(p):
    '''print_many2 : COMMA print_many
                   | empty'''


    
#<READ>
def p_read(p):
    '''read : READ LPAREN variable RPAREN'''

#<CYCLE>
def p_cycle(p):
    '''cycle : for
             | while'''
    
#<WHILE>
def p_while(p):
    '''while : DO body WHILE LPAREN exp RPAREN SEMICOLON'''

#<FOR>
def p_for(p):
    '''for : FOR LPAREN ID TO for_end RPAREN body SEMICOLON'''

def p_for_end(p):
    '''for_end : int_const_saver
               | ID'''


# <CALL_FUNCTION>
def p_call_function(p):
    '''call_function : function_saver LPAREN exp exp_many RPAREN '''
    #TEST 
    #print('factor funcion ', p[-1])

def p_function_saver(p):
    '''function_saver : ID empty'''
    global curr_name
    curr_name = p[1]
    #print('factor funcion ', curr_name)

#<EXP_MANY>
def p_exp_many(p):
    '''exp_many : COMMA exp exp_many
                | empty'''
    
#<STATEMENT>
def p_statement(p):
    '''statement : assign
                 | condition
                 | print
                 | cycle
                 | call_function'''

#<SPECIAL_FUNCTIONS>
def p_special_function(p):
    '''special_function : exploration
                        | financial_state
                        | dummi_regression
                        | season_analysis
                        | trend_prediction
                        | model_predict'''

    #<STATISTICAL_ANALYSIS>

#<EXPLORATION>
def p_exploration(p):
    '''exploration : EXPLORATION LPAREN variable explore_var explor_cte RPAREN'''

def p_explore_var(p):
    '''explore_var : COMMA variable
                   | empty'''  

def p_explor_cte(p):
    '''explor_cte : COMMA int_const_saver
                  | empty'''
    
#<FINANCIAL_STATE>
def p_financial_state(p):
    '''financial_state : FINANCIAL_STATE LPAREN variable COMMA variable COMMA variable COMMA variable RPAREN'''

#<SEASON_ANALYSIS>
def p_season_analysis(p):
    '''season_analysis : SEASON_ANALYSIS LPAREN variable RPAREN'''

    #<MACHINE LEARNING>

#<TREND_PREDICTION>
def p_trend_prediction(p):
    '''trend_prediction : TREND_PREDICTION LPAREN variable COMMA int_const_saver COMMA int_const_saver COMMA int_const_saver RPAREN'''

#<DUMMI_PREDICTION>
def p_dummi_regression(p):
    '''dummi_regression : DUMMI_REGRESSION LPAREN variable COMMA variable dr_array dr_int RPAREN'''

def p_dr_array(p):
    '''dr_array : COMMA LSQBRACKET CTE_CHAR dr_array_mp RSQBRACKET
                | empty'''

def p_dr_array_mp(p):
    '''dr_array_mp : COMMA CTE_CHAR dr_array_mp
                   | empty'''

def p_dr_int(p):
    '''dr_int : COMMA int_const_saver
              | empty'''
    
#<MODEL_PREDICT>
def p_model_predict(p):
    '''model_predict : MODEL_PREDICT LPAREN variable COMMA variable COMMA RPAREN'''


#__________________________________<EXP>___________________________
def p_exp(p):
    '''exp : t_exp release_exp exp_or'''
#CORRECCION :  SE CAMBIO DE LUGAR release_exp
#ANTERIORMENTE ESTABA ABAJO \/
def p_exp_or(p):
    '''exp_or : exp_keep_or  exp
              | empty'''
    
def p_exp_keep_or(p):
    '''exp_keep_or : OR'''
     #NEURALGIC POINT 2
     #Se coloca p[-1] para que s 
    print("exp_keep_or\n\n" , p[1])
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))

#_________________________________<T_EXP>_____________________________________
def p_t_exp(p):
    '''t_exp : expression release_exp t_exp_and'''
    global g_test
    g_test = 10

def p_t_exp_and(p):
    '''t_exp_and : keep_and t_exp
                 | empty'''

def p_keep_and(p):
    '''keep_and : AND '''
    #NEURALGIC POINT 2
    #CORRECCION : SE CAMBIO EL EMPTY POR AND PARA QUE FUERA MAS FACIL
    #ENVIAR LOS DATOS, EN LUGAR DE MANDAR P[-1] SE MANDA P[1]
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
  
#____________________________________<EXPRESSION>___________________________________
def p_expression(p):
    '''expression : m_exp release_exp expression_comp'''
    global g_test
    g_test = 9
    print("expression")

def p_expression_comp(p):
    '''expression_comp :  expression_comp_2  m_exp release_exp
                       | empty'''
    print("expression_comp", p[1])
    

def p_expression_comp_2(p):
    '''expression_comp_2 : GTHAN
                         | EQUAL
                         | NOTEQUAL
                         | LTHAN
                         '''
     #NEURALGIC POINT 2
    
    print("expression_comp_2", p[1])
    
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))

#__________________________________<M_EXP>_________________________________________
def p_m_exp(p):
    '''m_exp : term release_exp m_exp_sr'''
    global g_test
    #Valor de not equal
    g_test = 24
    #print("m_exp")

def p_m_exp_sr(p): 
    '''m_exp_sr : m_exp_sr_2 m_exp
                | empty'''

def p_m_exp_sr_2(p):
    '''m_exp_sr_2 : PLUS
                  | MINUS'''
     #NEURALGIC POINT 2
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
    
#____________________________________<TERM>__________________________________
#PC -> PRODUCTO - COCIENTE
def p_term(p):
    '''term : sub_factor release_exp term_pc'''
    global g_test
    g_test = 11
    #print("term")

def p_term_pc(p):
    '''term_pc : term_pc_2 term
               | empty'''

def p_term_pc_2(p):
    '''term_pc_2 : MULTIPLY
                 | DIVIDE
                 | MODULE'''
    #NEURALGIC POINT 2
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
#____________________________________<SUB_FACTOR>____________________________________
def p_sub_factor(p):
    '''sub_factor : factor release_exp sub_factor_pc'''
    global g_test
    #Valor de Multiplicativo
    g_test = 15

def p_sub_factor_pc(p):
    '''sub_factor_pc : sub_factor_pc_2 sub_factor
                     | empty'''

def p_sub_factor_pc_2(p):
    '''sub_factor_pc_2 : POWER empty'''
    #NEURALGIC POINT 2
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
  
#_____________________________<FACTOR>______________________________

def p_factor(p):
    '''factor : factor_exp
              | factor_cte
              | variable
              | call_function'''
    global g_test
    #Valor de la potencia
    g_test = 16

def p_factor_exp(p):
    '''factor_exp : false_button exp release_false_button'''

#_______NEURALGIC POINT_____ PARENTESIS

def p_false_button(p):
    '''false_button : LPAREN'''
    #NEURALGIC POINT 1
    print("false_button")
    quad.false_button()

def p_release_false_button(p):
    '''release_false_button : RPAREN'''
    #NEURALGIC POINT 1
    quad.release_false_button()

#_______NEURALGIC POINT_____ END PARENTESIS

def p_factor_cte(p):
    '''factor_cte : CTE_FLOAT
                  | CTE_INT
                  | CTE_CHAR'''
    global  curr_name
    curr_name = p[1]
    tables.add_const(p[1], type (p[1]))
    type_test = type(p[1]).__name__
    if(type_test == 'str'):
        type_test = 'char'
    const_type = oracle.datalor_translator(type_test.upper())
    quad.type_stack_push(const_type)
    quad.operands_stack_push(curr_name)
    print('Const ',curr_name , type_test, const_type)

# Build the parser
parser = yacc.yacc()

#TEST CON ARCHIVOS

if __name__ == '__main__':

    if len(sys.argv) > 1:
        file = sys.argv[1]
        try:
            f = open(file, 'r')
            data = f.read()
            f.close()
            if yacc.parse(data) == "COMPILED":
                print("Input aceptado")
        except EOFError:

            print(EOFError)
    else:
        print("No se encontro el archivo")