# ------------------------------------------------------------
# DATALOR: PARSER
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# PASER.... 
# ------------------------------------------------------------
import ply.yacc as yacc
from lexer import tokens
import sys


#Grammar declaration

#<PROGRAM>
def p_program(p):
    '''program : PROGRAM ID SEMICOLON program_libraries program_vars program_function program_main END'''
    p[0] = "COMPILED"

#EMPTY
def p_empty(p):
    'empty : '
    pass

#<LIBRERIES>
#Uso de las librerias en el programa  
  
def p_program_libraries(p):
    '''program_libraries : from_library import_library 
                         | empty'''

def p_from_library(p):
    '''from_library : FROM ID
                    | empty'''

def p_import_library(p):
    '''import_library : IMPORT ID AS ID  program_libraries'''   

#VARIABLES
#Uso de las variables en el programa
def p_var_type(p):
    '''var_type : var_c_type
                | var_s_type'''

def p_program_vars(p):
    '''program_vars : VAR var_type  
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
    '''c_type : DATAFRAME
              | DATE'''
    

def p_var_multiple(p):
    '''var_multiple : var_type
                    | empty'''

def p_var_c_type(p):
    '''var_c_type : c_type ID var_c_type2 SEMICOLON var_multiple'''

def p_var_c_type2(p):
    '''var_c_type2 : COMMA ID var_c_type2
                   | empty'''
    
def p_var_s_type(p):
    '''var_s_type : s_type ID var_s_array var_s_type2 SEMICOLON var_multiple'''

def p_var_s_type2(p):
    '''var_s_type2 : COMMA ID var_s_array var_s_type2
                   | empty'''

def p_var_s_array(p):
    '''var_s_array : LSQBRACKET CTE_INT RSQBRACKET var_s_matrix
                   | empty'''

def p_var_s_matrix(p):
    '''var_s_matrix : LSQBRACKET CTE_INT RSQBRACKET
                    | empty'''

def p_variable(p):
    '''variable : ID variable_array
                | empty'''

def p_variable_array(p):
    '''variable_array : LSQBRACKET exp RSQBRACKET variable_matrix
                      | empty'''

def p_variable_matrix(p):
    '''variable_matrix : LSQBRACKET exp RSQBRACKET
                       | empty'''
    
#FUNCTIONS
#Uso de las funciones en el programa
def p_program_function(p):
    '''program_function : FUNCTION function_type ID LPAREN param RPAREN LBRACKET inner_body return RBRACKET'''

def p_function_type(p):
    '''function_type : s_type
                    | VOID'''
    
#<PARAM>
def p_param(p):
    '''param : s_type ID param2'''

def p_param2(p):
    '''param2 : COMMA s_type ID param2
              | empty'''

#<RETURN>
def p_return(p):
    '''return : RETURN var_cte SEMICOLON
              | empty'''

#Uso del main en el programa
def p_program_main(p):
    '''program_main : MAIN LBRACKET inner_body RBRACKET'''


#<BODY>
def p_body(p):
    '''body : LBRACKET inner_body RBRACKET'''

#<INNER_BODY>
def p_inner_body(p):
    '''inner_body : program_vars inner_body2'''

def p_inner_body2(p):
    '''inner_body2 : statement inner_body2
                   | empty'''

#<ASSIGN>
def p_assign(p):
    '''assign : variable ASSIGN exp SEMICOLON'''

#<CONDITION>
def p_condition(p):
    '''condition : IF LPAREN exp RPAREN body condition2 SEMICOLON'''

def p_condition2(p):
    '''condition2 : ELSE body
                 | empty'''
    
#<PRINT>
def p_print(p):
    '''print : PRINT LPAREN print_many RPAREN SEMICOLON'''
    
#Notas modificar print para que sirva con exp en ID
def p_print_type(p):
    '''print_type : ID
                  | CTE_CHAR'''

def p_print_many(p):
    '''print_many : print_type print_many2 '''

def p_print_many2(p):
    '''print_many2 : COMMA print_type print_many2
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
    '''for_end : CTE_INT
               | ID'''

# <CALL_FUNCTION>
def p_call_function(p):
    '''call_function : ID LPAREN exp exp_many RPAREN'''

#<EXP_MANY>
def p_exp_many(p):
    '''exp_many : COMMA exp exp_many
                | empty'''
    
#<STATEMENT>
def p_statement(p):
    '''statement : assign
                 | condition
                 | print
                 | read
                 | cycle
                 | call_function
                 | special_function'''

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
    '''explor_cte : COMMA CTE_INT
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
    '''trend_prediction : TREND_PREDICTION LPAREN variable COMMA CTE_INT COMMA CTE_INT COMMA CTE_INT RPAREN'''

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
    '''dr_int : COMMA CTE_INT
              | empty'''
    
#<MODEL_PREDICT>
def p_model_predict(p):
    '''model_predict : MODEL_PREDICT LPAREN variable COMMA variable COMMA RPAREN'''


#<EXP>
def p_exp(p):
    '''exp : t_exp exp_or'''

def p_exp_or(p):
    '''exp_or : OR exp
              | empty'''

#<T_EXP>
def p_t_exp(p):
    '''t_exp : expression t_exp_and'''

def p_t_exp_and(p):
    '''t_exp_and : AND t_exp
                 | empty'''
    
#<EXPRESSION>
def p_expression(p):
    '''expression : m_exp expression_comp'''

def p_expression_comp(p):
    '''expression_comp : expression_comp_2 m_exp
                       | empty'''

def p_expression_comp_2(p):
    '''expression_comp_2 : EQUAL
                         | NOTEQUAL
                         | LTHAN
                         | GTHAN'''


#<M_EXP>
def p_m_exp(p):
    '''m_exp : term m_exp_sr'''

def p_m_exp_sr(p): 
    '''m_exp_sr : m_exp_sr_2 m_exp
                | empty'''

def p_m_exp_sr_2(p):
    '''m_exp_sr_2 : PLUS
                  | MINUS'''
    
#<TERM>
def p_term(p):
    '''term : factor term_pc'''

def p_term_pc(p):
    '''term_pc : term_pc_2 term
               | empty'''

def p_term_pc_2(p):
    '''term_pc_2 : MULTIPLY
                 | DIVIDE'''
    
#<FACTOR>

def p_factor(p):
    '''factor : factor_exp
              | factor_cte
              | variable
              | call_function'''

def p_factor_exp(p):
    '''factor_exp : LPAREN exp RPAREN'''

def p_factor_cte(p):
    '''factor_cte : CTE_INT
                  | CTE_FLOAT
                  | CTE_CHAR'''


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