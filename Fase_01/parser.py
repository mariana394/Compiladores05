# ------------------------------------------------------------
# DATALOR: PARSER
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# PARSER.... 
# ------------------------------------------------------------
import ply.yacc as yacc
from lexer import tokens
import sys
from func_var_tables import DirFunc
from quadruples import Quadruples
from dictionary import Dictionary
from special_functions import special_functions
from virtualmachine import VirtualMachine

#Global variables
curr_type = ''
scope = 0 
curr_name = ''
curr_function = 'global'
# GB for arrays and Matrix
curr_rows = 0
curr_columns = 0
curr_dim = 0 #por si las moscas
curr_temp = 0
g_test = 10
curr_variable = ''
curr_const = None
for_flag = False
return_flag = False
function_flag = False #False for normal variables, true for functions
era_stack = []


#Objects
tables = DirFunc()
quad = Quadruples()
oracle = Dictionary()
special = special_functions()
vm = VirtualMachine()




#__________________________<PROGRAM>_________________________
def p_program(p):
    '''program : PROGRAM ID goto_main program_libraries program_vars program_function program_main end '''
    p[0] = "COMPILED"

def p_goto_main(p):
    '''goto_main : SEMICOLON'''
    tables.add_const(1,type(1))
    quad.insert_goto(16)

def p_end(p):
    '''end : END '''
    global curr_function
    quad.quadruple.append([41,0,0,0])
    curr_function = 'main'
    print("RESOURCES DONE")
    print("CURR_ FUNCTION", curr_function)
    tables.resources_handler(curr_function)
    tables.add_resources_temp(quad.t_i_cont,quad.t_f_cont, quad.t_b_cont, quad.t_c_cont, quad.t_df_cont,quad.t_tp_cont, curr_function)
    
    print(quad.print_poperands())
    all_quad = quad.get_quad()
    res = tables.get_func_res()
    const = tables.constants
    vm.set_quadruples(all_quad)
    vm.set_const(const)
    vm.set_resources(res)
    print("RESS MAIN", res[1])
    vm.start_vm()

    
    #print()
    

    # ovejota = None
    # tables.add_func_resources_glob()
    # cuadruplos = quad.print_poperands()
    # print("CUADRUPLOS", cuadruplos)
    # dir = tables.print()
    # const = tables.get_const()
    # ovejota = "&&" + str(dir) + "&&" + str(const)
    # with open('intermedio.txt', 'w') as filehandle:
    #     for listitem in quad.quadruple:
    #         filehandle.write(f'{listitem}\n')
    #     filehandle.write(ovejota)


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
    '''int_const_saver : CTE_INT 
                       | empty'''
    global curr_const, for_flag
    curr_const = p[1]
    for_flag = True
    address = tables.add_const(curr_const, type (curr_const))
    print("constante for ", curr_const)
    
    quad.operands_stack_push(address)
    quad.type_stack_push(oracle.datalor_translator(type(curr_const).__name__.upper()))

#Neuralgic point number 1 for all expressions where we check first if we have a pending operator
def p_release_exp(p):
    '''release_exp : empty'''
    global g_test
    #print ("Tipo de Operacion", g_test)
    quad.create_exp_quadruple(g_test)

def p_resources(p):
    '''resources : empty'''
    global curr_function, era_stack
    tables.resources_handler(curr_function)
    tables.add_resources_temp(quad.t_i_cont,quad.t_f_cont, quad.t_b_cont, quad.t_c_cont, quad.t_df_cont,quad.t_tp_cont, curr_function)
    #SI EN NUESTRA PILA DE ERA HAY ALGO RELLENA
    #Llamar a los recursos de curr_function
    #Int - float- char- bool- df- 
    res = tables.get_resources(curr_function)
    print("MARTES NOCHE", res)
    if(len(era_stack) != 0):
        for i in range(len(era_stack)):
            #Int - t_INT
            quad.quadruple[era_stack[i]] = [35, '', res[0], res[5]]
            #FLOAT - t_FLOAT
            quad.quadruple[era_stack[i]+ 1] = [35, '', res[1], res[6]]
            
            #BOOL - t_BOOOL
            quad.quadruple[era_stack[i]+ 3] = [35, '', res[3], res[8]]
            
            #CHAR - t_CHAR
            quad.quadruple[era_stack[i]+ 2] = [35, '', res[2], res[7]]
            
            #DATAFRAME - t_DATAFRAME
            quad.quadruple[era_stack[i]+ 4] = [35, '', res[4], res[9]]
            #POINTER
            quad.quadruple[era_stack[i]+ 5] = [35, '', '', res[10]]

    quad.reset_temp()

# flag check for knowing if its is a variabel or a function
def check_flag_func():
    global function_flag
    if(function_flag):
        print("ERROR: Function name used as a variable")
        exit()
    else:
        print("toy chiquito no puedo")


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
    global curr_name
    print("arreglo", p[1])

def p_var_s_matrix(p):
    '''var_s_matrix : LSQBRACKET var_s_dimesions RSQBRACKET
                    | empty'''
    print("matriz", p[1])
#____NEURALGIC POINT______#
def p_var_s_dimesions(p):
    '''var_s_dimesions : CTE_INT empty'''
    global curr_rows, curr_columns
    #____Classifying s_type variables____#
    #Add the size as a constant in the constants variable
    address = tables.add_const(p[1], type(p[1]))
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
    '''variable : var_id_saver variable_array clear_dimension'''
    
def p_clear_dimension(p):
    '''clear_dimension : empty'''
    global curr_dim
    curr_dim = 0
    quad.release_false_button()

def p_var_id_saver(p):
    ''' var_id_saver : id_saver'''    
    global curr_name, scope, function_flag, curr_variable
    #print("var m ", curr_name)
    curr_variable = curr_name
    if(tables.search_func_exist(curr_name)):
        function_flag = True
    else:
        function_flag = False
    type = []
    #TEST1
    print("false_button")
    quad.false_button()
    print("variable antes ", curr_name)
    type = tables.search_variable_existance(curr_name, scope)
    print("variable ", curr_name, type)
    quad.type_stack_push(type[0])
    quad.operands_stack_push(type[1])

    #print(scope, ' factor variable ', curr_name, type )

def p_variable_array(p):
    '''variable_array : LSQBRACKET index_arr_mat RSQBRACKET variable_matrix
                      | empty'''
    check_flag_func()
    
    
        
    
def p_variable_matrix(p):
    '''variable_matrix : LSQBRACKET index_arr_mat RSQBRACKET
                       | empty'''


def p_index_arr_mat(p):
    '''index_arr_mat : exp'''
    global curr_dim, scope,curr_variable
    curr_dim += 1
    size = tables.get_arr_mat_info(curr_variable, scope)
    quad.arr_mat_quad(size, curr_dim)
    

    
#_________________________________________FUNCTIONS______________________________________#
#
#Program functions 
def p_program_function(p):
    '''program_function : FUNCTION resources f_type id_saver func_creator  LPAREN param RPAREN add_func_glob program_vars inner_body return end_function program_function
                        | empty'''


#type of funtion return
def p_f_type(p):
    '''f_type : INT 
              | FLOAT
              | CHAR
              | VOID'''
    global curr_type,scope,return_type
    curr_type = p[1]
    return_type = curr_type
    scope += 1
    
   
    
    #print(curr_type,scope)
#______FUNCTION___NEURALGIC POINTS________#

def p_func_creator(p):
    '''func_creator : empty'''
    global scope, curr_function, curr_type, curr_name
    curr_function = curr_name
    start = quad.cont_place()
    print ("func_creator", curr_function, scope, curr_type, start)
    tables.add_vars(curr_function,0,return_type)
    tables.add_function(curr_name,scope,curr_type, start)


def p_add_func_glob(p):
    '''add_func_glob : LBRACKET'''
    global curr_function,scope, return_type,function_flag, curr_name, curr_type
    #tables.memory_num = quad.cont_place()

    #Idea de nosotros donde guardaba tipo funcion
    # y a donde debe de saltar
    #tables.add_vars(curr_function,0,6)

def p_end_function(p):
    '''end_function : RBRACKET'''

    quad.end_func_quad()
    
#_____________________________________________________

#_________________________<PARAM>__________________________#
def p_param(p):
    '''param : s_type id_saver add_params param2
             | empty'''
    print("PARAMETRO")    

def p_param2(p):
    '''param2 : COMMA s_type id_saver add_params param2
              | empty'''
    print("PARAMETRO 2")
#________PARAMS NEURALGIC POINTS___________________________
def p_add_params(p):
    '''add_params : empty'''
    global curr_type, curr_name, scope, curr_function
    tables.add_vars(curr_name,scope,curr_type)
    print("parametros", curr_name, scope, curr_type, curr_function)
    tables.add_params(curr_function,curr_type)

#_________________________<RETURN>____________________#
def p_return(p):
    '''return : return_np exp return_quad SEMICOLON
              | empty_path_return'''

def p_return_np(p):
    '''return_np : RETURN'''
    global return_type
    if(return_type != 'void'):
        print("okay")
    else:
        print("ERROR: FUNCTION IS VOID: NON-VALUE RETURNING FUNCTION")
        exit()

def p_return_quad(p):
    '''return_quad : empty'''
    global return_type, curr_function
    #Needs to be used address instead only name
    address = []
    address = tables.search_variable_existance(curr_function, 0)
    quad.return_quad(return_type, address[1])

# Void function for empty path
def p_empty_path_return(p):
    '''empty_path_return : empty'''
    global return_type
    if(return_type == 'void'):
        print("okay")
    else:
        print("ERROR: FUNCTION MUST HAVE RETURN STATEMENT")
        exit()

#____________________MAIN_________________#
#Uso del main en el programa
def p_program_main(p):
    '''program_main :  main_id LBRACKET program_vars inner_body RBRACKET'''

def p_main_id(p): 
    '''main_id : MAIN resources '''
    global scope, curr_function
    scope += 1
    curr_function = 'main'
   # print("TIPOO JUMPS", quad.jump_stack_pop())
    quad.fill(quad.jump_stack_pop()-1,quad.cont_place())
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
   #PRINT
   
def p_specialf_assign(p):
    '''specialf_assign : exp
                       | special_function
                       | read'''
    
#keep the assign -> STACK
def p_keep_assign(p):
    '''keep_assign : ASSIGN empty'''
    global curr_name, scope
    #print('ASSIGN H ', curr_name)
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
    global function_flag
    quad.assign_quadruple()
    check_flag_func()


#_________________________<CONDITION>___________________________________
def p_condition(p):
    '''condition : IF LPAREN exp RPAREN condition_GOTOF body condition2 SEMICOLON end_condition'''

def p_condition2(p):
    '''condition2 : ELSE condition_GOTO body
                 | empty'''

# Neuralgic point 1
def p_condition_GOTOF(p):   
    '''condition_GOTOF : empty'''
    print('\t\tcondition_GOTOF\n')
    quad.jump_stack_push()
    quad.insert_goto(18)

#Neuralgic point 2
def p_condition_GOTO(p):   
    '''condition_GOTO : empty'''
    print('\t\tcondition_GOTO\n')
    quad.insert_goto(17)

def p_end_condition(p):
    '''end_condition : empty'''
    jump = quad.jump_stack_pop()
    where = quad.cont_place()
    quad.fill(jump, where)


    
#_________________________<PRINT>____________________
def p_print(p):
    '''print : PRINT LPAREN print_many RPAREN SEMICOLON end_print_np'''
    
def p_print_type(p):
    '''print_type : exp'''

def p_print_many(p):
    '''print_many : print_type print_many2 '''

def p_print_many2(p):
    '''print_many2 : COMMA print_many_np print_many
                   | empty'''
    
def p_print_many_np(p):
    '''print_many_np : empty'''
    quad.print_quadruple()

def p_end_print_np(p):
    '''end_print_np : empty'''
    quad.print_quadruple()
    
    
#________________________<READ>_______________________
def p_read(p):
    '''read : np_read LPAREN valid_exp_read read_np'''

def p_np_read(p):
    '''np_read : READ'''

def p_valid_exp_read(p):
    '''valid_exp_read : exp'''
    #CHECK TOP OF THE STACK
    type_exp = quad.type_stack_pop()
    print('PRINT END', type_exp)
    if (type_exp != 3 ):
        print('ERROR: Only char parameters are allowed')        
        exit()

def p_read_np(p):
    '''read_np : RPAREN'''
    
    value = quad.operands_stack_pop()
    print("SI LLEGA AL READ", value)
    quad.read_quadruple(value)

#_____________________<CYCLE>_________________
def p_cycle(p):
    '''cycle : for
             | while'''
    
#___________________<WHILE>______________________
def p_while(p):
    '''while : DO seed body WHILE LPAREN exp RPAREN SEMICOLON gotoV'''

#neuralgic point 1 (guardar la semilla de a donde regreso)
def p_seed(p):
    '''seed : empty'''
    quad.jump_seed()
    
#Neuralgic point 2
def p_gotoV(p):
    '''gotoV : empty'''
    quad.insert_goto(19)


#_________________<FOR>____________
def p_for(p):
    '''for : FOR LPAREN for_control keep_assign exp for_np1 for_end body for_np2'''

def p_for_control(p):
    '''for_control : id_saver'''
    global curr_name, scope 
    type = tables.search_variable_existance(curr_name, scope)
    quad.type_stack_push(type[0])
    quad.operands_stack_push(type[1])
    


def p_for_np1(p):
    '''for_np1 :  TO'''
    quad.control_var()


def p_for_end(p):
     '''for_end : int_const_saver RPAREN'''
     quad.final_var()
     #Se inserta un 32 para que se haga la comparacion
     #quad.print_poperands()
     quad.operators_stack_push(31)
     quad.create_exp_quadruple(31)
     quad.jump_stack_push()
     quad.insert_goto(18)
     quad.jump_stack_push()



def p_for_np2(p):
    '''for_np2 : SEMICOLON'''
    quad.end_for()

# # def p_for(p):
# #     '''for : FOR LPAREN id_saver for_np1 TO for_end  RPAREN body SEMICOLON'''


# def p_for_end(p):
#     '''for_end : int_const_saver
#                | ID '''
#     print('\t\tSEGUNDO PUNTO\n', p[1])
    


# def p_for_np1(p):
#     '''for_np1 : TO'''
#     global curr_name, scope
#     type = tables.search_variable_existance(curr_name, scope)
#     quad.type_stack_push(str(type))
#     quad.operands_stack_push(curr_name)
#     quad.check_integer()
#     quad.control_var()
#     #Insert the operator that represents "TO"
#     quad.operators_stack_push(32)
    
    
#     #print('\t\tPRIMER PUNTO\n', curr_name, scope)

# def p_for_np2(p):
#     '''for_np2 : RPAREN'''
#     global curr_name, curr_const,scope, for_flag
#     if (for_flag == True):
#         quad.type_stack_push('28')
#         quad.operands_stack_push(curr_const)
#         for_flag = False
#     else:
#         tipo = tables.search_variable_existance(curr_name, scope)
#         quad.type_stack_push(str(tipo))
#         quad.operands_stack_push(curr_name)
#         quad.check_integer()
#     quad.create_exp_quadruple()
    
    

#____________________________<CALL_FUNCTION>___________________________#
def p_call_function(p):
    '''call_function : function_saver function_flag call_params check_not_void '''
    #TEST 
    #print('factor funcion ', p[-1])

def p_check_not_void(p):
    '''check_not_void : RPAREN'''
    global return_flag, curr_function
    print("return flag ", return_flag)
    if (return_flag == True):
        print("ERROR: Function must not be part of an expression")
        exit()
    #CHECK AMOUNT OF PARAMETERS   
    params_len = tables.get_size_param(curr_function)
    print("entro al verificador", params_len, quad.param_cont-1)
    if(params_len > quad.param_cont-1):
        print("PARAMETERSssssss",params_len)
        print("ERROR: MISSING PARAMETERS ")
        exit()
    #Inserts Gosub for void function
    quad.insert_goto(36,tables.dir_func[curr_function]["start"])
    
    


#______________CALL VOID FUNCTION______________________#

def p_call_void_function(p):
    '''call_void_function : function_saver function_flag call_params verify_params check_void'''

def p_verify_params(p):
    '''verify_params : RPAREN'''
    global curr_function 
    params_len = tables.get_size_param(curr_function)
    print("entro al verificador", params_len, quad.param_cont-1)
    if(params_len > quad.param_cont-1):
        print("2.PARAMETERSssssss",params_len)
        print("ERROR: MISSING PARAMETERS ")
        exit()
    
def p_check_void(p):
    '''check_void : SEMICOLON'''
    global return_flag, curr_function
    #CHECK FOR VOID FUNCTION
    if (return_flag == False):
        print("ERROR: Function must be part of an expression")
        exit()
    else:
        return_flag = False
    #Inserts Gosub for void function
    quad.insert_goto(36,tables.dir_func[curr_function]["start"])
    
    
#____________-GENERIC CALL FUNCTIONS_________+
def p_function_saver(p):
    '''function_saver : ID empty'''
    global curr_name, curr_type , function_flag, curr_function
    curr_name = p[1]
    #Test
    curr_function = curr_name
    #LOOK FOR FUNCTION EXISTANCE
    function_flag = tables.search_func_exist(curr_name)
    #It is after return_type becuase it will exit in case
    #the function does not exist and will continue if it does
    print('factor funcion ', curr_name)

def p_function_flag(p):
    '''function_flag : LPAREN'''
    global function_flag, curr_name, return_type, return_flag, era_stack
    function_flag = False
    
    type= []
    type = tables.search_variable_existance(curr_name, scope)
    quad.type_stack_push(type[0])
    quad.operands_stack_push(type[1])
    
    if (type[0] == 6):
        return_flag = True 
    era_resource = tables.get_resources(curr_name)
    print("TEST",len(era_resource))
    if (len(era_resource) != 0 ):
        quad.create_era(era_resource)
    else:
        #guardar donde estoy en la pila de ERAs
        era_stack.append (quad.cont-1)
        #Int
        quad.quadruple.append([])
        quad.cont += 1
        #Float
        quad.quadruple.append([])
        quad.cont += 1
        #Bool
        quad.quadruple.append([])
        quad.cont += 1
        #Char
        quad.quadruple.append([])
        quad.cont += 1
        #DF
        quad.quadruple.append([])
        quad.cont += 1
        #POINTER
        quad.quadruple.append([])
        quad.cont += 1
        quad.param_cont = 1

    


def p_call_params(p):
    '''call_params : check_param exp_many
                   | empty'''
    

#_________EXP_______
def p_check_param(p):
    '''check_param : exp'''
    global curr_function
    param = quad.operands_stack_pop()
    param_type = quad.type_stack_pop()
    print ("param ", param, param_type)
    tables.check_param(param_type, quad.param_cont, curr_function)
    quad.quadruple.append([37, param, '', quad.param_cont])
    quad.cont += 1
    quad.param_cont += 1



#______<EXP_MANY>
def p_exp_many(p):
    '''exp_many : COMMA check_param exp_many
                | empty'''
    
#<STATEMENT>
def p_statement(p):
    '''statement : assign
                 | condition
                 | print
                 | cycle
                 | call_void_function'''

#<SPECIAL_FUNCTIONS>
def p_special_function(p):
    '''special_function : exploration
                        | financial_state
                        | dummi_regression
                        | season_analysis
                        | trend_prediction
                        | model_predict'''

#__________GENERIC SPECIAL FUNCTIONS GRAMMAR_______
#tag_sp -> tag special function
def p_tag_sp(p):
    '''tag_sp : LPAREN'''
    global curr_function
    curr_function = p[-1]
    #Inicializa el contador de parametros en 1
    quad.param_cont = 1
    print("TAMOS PROBANDO", p[-1])
    quad.quadruple.append(['special','','',curr_function])
    quad.cont += 1

#____________<STATISTICAL_ANALYSIS>_____________

#_______________<EXPLORATION>________________
def p_exploration(p):
    '''exploration : EXPLORATION tag_sp variable explore_cte np_check_size'''

def p_sp_param(p):
    '''sp_param : COMMA'''
    global curr_function
    param = quad.param_cont
    #Check tipy for special function params
    
    tipo = quad.type_stack_pop()
    value = quad.operands_stack_pop()
    print("PARAMETROS", tipo , value)
    print("ESTOY DENTRO DE LA COMA", tipo)
    special.search_sf_param(curr_function, param, tipo)
    
    
    quad.quadruple.append([37,value,'',param])
    quad.cont += 1 
    quad.param_cont += 19

def p_np_check_size(p):
    '''np_check_size : RPAREN'''
    global curr_function
    param = quad.param_cont
    #Check tipy for special function params
    print('Operadores', quad.pOperands)
    
    tipo = quad.type_stack_pop()
    value = quad.operands_stack_pop()
    print("ESTOY DENTRO DE LA COMA", tipo)

    special.search_sf_param(curr_function, param, tipo)
    
    print("PARAMETROS", tipo , value)

    #
    quad.quadruple.append([37,value,'',param])
    quad.cont += 1 
    memory = quad.t_df_cont + quad.t_df_init
    quad.t_df_cont += 1
    quad.insert_goto(38,memory)
    quad.operands_stack_push(memory)
    quad.type_stack_push(5)


def p_explore_cte(p):
    '''explore_cte : sp_param int_const_saver
                  | empty'''
    
    
#__________<FINANCIAL_STATE>__________
def p_financial_state(p):
    '''financial_state : FINANCIAL_STATE tag_sp variable sp_param variable sp_param variable sp_param variable np_check_size'''

#___________<SEASON_ANALYSIS>_______
def p_season_analysis(p):
    '''season_analysis : SEASON_ANALYSIS tag_sp variable np_check_size'''

    #<MACHINE LEARNING>

#_____________<TREND_PREDICTION>_____________
def p_trend_prediction(p):
    '''trend_prediction : TREND_PREDICTION tag_sp variable sp_param int_const_saver sp_param int_const_saver sp_param int_const_saver np_check_size'''

#_____________<DUMMI_PREDICTION>__________________
def p_dummi_regression(p):
    '''dummi_regression : DUMMI_REGRESSION tag_sp variable sp_param variable dr_array dr_int np_check_size'''

def p_dr_array(p):
    '''dr_array : COMMA LSQBRACKET CTE_CHAR dr_array_mp RSQBRACKET
                | empty'''

def p_dr_array_mp(p):
    '''dr_array_mp : COMMA CTE_CHAR dr_array_mp
                   | empty'''

def p_dr_int(p):
    '''dr_int : COMMA int_const_saver
              | empty'''
    
#____________<MODEL_PREDICT>___________
def p_model_predict(p):
    '''model_predict : MODEL_PREDICT tag_sp variable sp_param variable np_check_size'''


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
    check_flag_func()
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
    check_flag_func()
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
  
#____________________________________<EXPRESSION>___________________________________
def p_expression(p):
    '''expression : m_exp release_exp expression_comp'''
    global g_test
    g_test = 9
    print("expression")

def p_expression_comp(p):
    '''expression_comp :  expression_comp_2  m_exp release_exp
                       |  empty'''
    print("expression_comp", p[1])
    

def p_expression_comp_2(p):
    '''expression_comp_2 : GTHAN
                         | EQUAL
                         | NOTEQUAL
                         | LTHAN
                         | GORE
                         | LORE
                         '''
     #NEURALGIC POINT 2
    
    print("expression_comp_2", p[1])
    check_flag_func()
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
    check_flag_func()
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
    check_flag_func()
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
    check_flag_func()
    quad.operators_stack_push(oracle.datalor_translator_symbols(p[1]))
  
#_____________________________<FACTOR>______________________________

def p_factor(p):
    '''factor : factor_exp
              | factor_cte
              | variable
              | call_function'''
    global g_test
    #Valor de la potencia
    check_flag_func()
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
    address = tables.add_const(p[1], type (p[1]))
    type_test = type(p[1]).__name__
    if(type_test == 'str'):
        type_test = 'char'
    const_type = oracle.datalor_translator(type_test.upper())
    quad.type_stack_push(const_type)
    quad.operands_stack_push(address)
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