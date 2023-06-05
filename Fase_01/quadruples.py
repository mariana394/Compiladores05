# -----------------------------------------------------------
# DATALOR: CUADRUPLOS
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# Quadruples....
# -----------------------------------------------------------
from dictionary import Dictionary


oracle = Dictionary()


class Quadruples:
   
    #Inicialization
    def __init__(self):
        self.quadruple = []
        #We are always pointing one ahead of where we are
        self.cont = 1
        #_____________STACKS (LIFO)_________________#
        self.pOperators = []
        #Operands with type
        self.pOperands = []
        self.pJumps = []
        self.pSize = []
        self.pTypes = [] 

        #_____________TEMPORAL VARIABLES____________#
        #TEMPORALES
        self.t_i_size = 1999
        self.t_f_size = 1999
        self.t_c_size = 1999
        self.t_b_size = 1999
        self.t_df_size = 1999
        self.t_tp_size = 1999

        #START TEMPORALES
        self.t_i_init = 17000
        self.t_f_init = 19000
        self.t_c_init = 21000
        self.t_b_init = 23000
        self.t_df_init = 31000
        self.t_tp_init = 33000
        
        #COUNTER TEMPORALES
        self.t_i_cont = 0
        self.t_f_cont = 0
        self.t_c_cont = 0
        self.t_b_cont = 0 
        self.t_df_cont = 0
        self.t_tp_cont = 0


        #self.temp_cont = {} 

        self.param_cont = 0
   
   #_________________STACKS__________________
    #Function for size stac
    def size_stack_push(self, size):
        self.pSize.append(size)

    def size_stack_pop(self):
        return self.pSize.pop()

    #Function for opertors stack
    def operators_stack_push(self,operator):
        self.pOperators.append(operator)

    def operators_stack_pop(self):
        return self.pOperators.pop()

    #Function for operands stack
    def operands_stack_push(self,operand):
        self.pOperands.append(operand)

    def operands_stack_pop(self):
        return self.pOperands.pop()

    #TYPE STACK
    def type_stack_push(self,type):
        self.pTypes.append(type)

    def type_stack_pop(self):
        return self.pTypes.pop()
    
    #JUMP STACK
    def jump_stack_push(self):
        self.pJumps.append(self.cont - 1)
        print("")
    
    def jump_stack_pop(self):
        return self.pJumps.pop()
    
    def jump_seed(self):
        self.pJumps.append(self.cont)
    
    #CONT PLACE
    def cont_place(self):
        return self.cont

    #FONDO FALSO 
    def false_button(self):
        self.pOperators.append('(')
        print('fondo falso',self.pOperators)
    
    def release_false_button(self):
        print('release fondo falso',self.pOperators)
        if (len(self.pOperators) != 0):
            if(self.pOperators[-1] == '('):
                self.pOperators.pop()

    #FILL
    def fill(self, jump, place):
        print("ULTIMO FILL", jump, place)
        self.quadruple[jump][3] = place

    #<FOR> Control and final variables declaration
    def control_var(self ):
        self.check_integer()
        exp_type = self.type_stack_pop()
        exp = self.operands_stack_pop()
        self.size_stack_pop()
        #Se elige el valor y tipo para la variable de control
        vControl = self.pOperands[-1]
        control_type = self.pTypes[-1]
        #Se genera un espacio en memoria para la variable de control
        place = self.t_i_cont + self.t_i_init
        if (self.t_i_cont > self.t_i_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_i_cont += 1
        #Fin de asignacion de memoria
        #Se revisa si es posible la asignacion del ID y la expresion
        res = oracle.oracle_cmddwtm(str(exp_type),str(control_type),'21')
        print ("DE QUE TIPO ES", res)
        if (res != '1'):
            print("ERROR: TYPE MISMATCH")
            exit()
        else:
            self.quadruple.append([21, exp, '', vControl])
            self.cont += 1
            self.quadruple.append([21, vControl, '', place])
            self.cont += 1
            self.operands_stack_push(place)
            self.size_stack_push(0)
            self.type_stack_push(control_type)
            


    def final_var(self):
        self.check_integer()
        exp_type = self.type_stack_pop()
        exp = self.operands_stack_pop()
        self.size_stack_pop()
        #Se genera un espacio en memoria para la variable Final
        place = self.t_i_cont + self.t_i_init
        if (self.t_i_cont > self.t_i_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_i_cont += 1
        #Fin de asignacion de memoria
        igual = self.operators_stack_pop()
        self.quadruple.append([21, exp, '', place])
        self.cont += 1
        self.operands_stack_push(place)
        self.type_stack_push(exp_type)
        self.size_stack_push(0)

        print("FINAL FINAL", )
        #DUPLICAR LOS DATOS DE LA VARIABLE DE CONTROL Y LA VARIABLE FINAL
        vcontrol = self.pOperands[-2]
        #vfinal = self.pOperands[-1]
        control_type = self.pTypes[-2]
        #final_type = self.pTypes[-1]
        self.operands_stack_push(vcontrol)
        self.type_stack_push(control_type)
        self.size_stack_push(0)



    def end_for(self):
        vControl = self.operands_stack_pop()
        vControl_type = self.type_stack_pop()
        self.size_stack_pop()
        #Se genera un espacio para el incremento del la variable de control
        place = self.t_i_cont + self.t_i_init
        if (self.t_i_cont > self.t_i_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_i_cont += 1
        #Fin de asignacion de memoria
        #Se obtiene el lugar de donde se obtuvo el valor de la variable de control
        idfrom = self.operands_stack_pop()
        idfrom_type = self.type_stack_pop()
        self.size_stack_pop()
        #17000 because is the place where 1 is stored
        self.quadruple.append([11, vControl, 25000, place])
        self.cont += 1
        self.quadruple.append([21, place, '', vControl])
        self.cont += 1
        self.quadruple.append([21, place, '', idfrom])
        self.cont += 1


        fin = self.pJumps.pop()
        ret = self.pJumps.pop()
        self.quadruple.append([17, '', '', ret])
        self.cont += 1
        self.fill(fin-1, self.cont)

        
        
    #Function for creating quadruples
    def create_quadruple(self, operator, operandR, result = None, operandL = None):
        #CHECK SEMANTICS
        operator = oracle.datalor_translator(operator)
        operandR = oracle.datalor_translator()
        result = oracle.datalor_dictionary(result)
        operandL = oracle.datalor_translator(operandL)


        #oracle.semantics
    #______________________GENERIC FUNCT QUADRUPLE____________________#
    #Function to reset the temp values, which means you can use the same temp variables in other scope
    def reset_temp(self):
        self.t_i_cont = 0
        self.t_f_cont = 0
        self.t_c_cont = 0
        self.t_b_cont = 0 
        self.t_df_cont = 0
        self.t_tp_cont = 0 

    #_________________CHECKERS______________________#
                
    def check_bool(self):
        print("PILA DE OPERANDOS", self.pTypes)
        if(self.pTypes[-1] != '4'):
            print('Bool type was expected')
            exit()
            
    def check_integer(self):
        print("PILA DE OPERANDOS", self.pOperands)
        print("PILA DE TIPOS", self.pTypes)
        #print("CHECK", self.pTypes[-1])
        if(int(self.pTypes[-1]) != 1):
             print('Integer type was expected')
             exit()

    def check_const(self):
        print("PILA DE OPERANDOS", self.pOperands)
        print("PILA DE TIPOS", self.pTypes)
        if(self.pTypes[-1] != '28'):
            print('Constant Integer type was expected')
            exit()

    #Function to resolve EXP for queadruples 

    #_________________________ASSIGN__________________#
    def assign_quadruple(self):
        print(self.pOperators, self.pOperands, self.pSize)
       #POP from the tables for assigning it to the quadruple
        operator = self.operators_stack_pop()
        operandR = self.operands_stack_pop()
        size_opR = self.size_stack_pop()
        result = self.operands_stack_pop()
        size_result = self.size_stack_pop()
        print("DATOS",size_opR, size_result)
        if(size_opR != 0 or size_result !=0 and size_opR != None):
            print("DATOS2",size_opR, size_result)

            print("ERROR: ONLY ATOMIC ASSIGNS ARE ALLOWED")
            exit()

        print("VALORES A SUMAR",operandR, result )

       #POP to the types
        #print(self.pTypes)
        typeR = self.type_stack_pop()
        typeRes = self.type_stack_pop()
        #ASK THE ORACLE IF MDDWTM

        oracle_answer = oracle.oracle_cmddwtm(str(typeRes),str(typeR),str(operator))
        print("Oracle answer",oracle_answer)
       #CREATING THE CUADRUPLE
        self.quadruple.append([operator, operandR,'',result])
        self.cont += 1
        print("\t\tCONTADOR\t", self.cont)
        print(self.quadruple)
        

    #FUNCTION FOR ASSIGNING THE VARIABLES THAT ARE GOING TO BE PASSED TO THE QUADRUPLE 
    def inner_quad_exp(self):
        print('Lista de operandos', self.pOperands)
        print('Lista de Tipos', self.pTypes)
        print('LISTA DE SIZE', self.pSize)
        operandR = self.operands_stack_pop()
        size_right = self.size_stack_pop()

        typeR = self.type_stack_pop()
       
        operandL = self.operands_stack_pop()
        size_left = self.size_stack_pop()
        typeL = self.type_stack_pop()
        
        operator = self.operators_stack_pop()
        size = 0
        #ASK TO THE ORACLE
        print('operator', operator)
        type_result = oracle.oracle_cmddwtm(str(typeL),str(typeR),str(operator))
        self.pTypes.append(type_result)

        #ASK SIZE
        #Bothe are variadbles
        
        print('SIZE OF EXPRESSIONS', "RIGHT ",size_right,"LEFT",size_left )
        if(size_right != 0 or size_left != 0):
            print("ERROR: ONLY ATOMIC SIZES ARE AVAILABLE FOR EXPRESSIONS ")
            exit()
        

        

        
        #print('type_result', type(type_result))
        match type_result:
            #INTEGER
            case '1':
                if (self.t_i_cont > self.t_i_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_i_init + self.t_i_cont
                    self.t_i_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    print("\t\tCONTADOR\t", self.cont)
                    print(self.quadruple)
                    self.size_stack_push(0)

                    #print ('OPERANDOS',self.pOperands)
            #FLOAT
            case '2':
                if (self.t_f_cont > self.t_f_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_f_init + self.t_f_cont
                    self.t_f_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    print("\t\tCONTADOR\t", self.cont)
                    print(self.quadruple)
                    self.size_stack_push(0)

                    #print ('OPERANDOS',self.pOperands)
            #CHAR
            case '3':
                if (self.t_c_cont > self.t_c_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_c_init + self.t_c_cont
                    self.t_c_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    print("\t\tCONTADOR\t", self.cont)
                    print(self.quadruple)
                    self.size_stack_push(0)

                    #print ('OPERANDOS',self.pOperands)
            #BOOLEAN
            case '4':
                print('entro a boolean')
                if (self.t_b_cont > self.t_b_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_b_init + self.t_b_cont
                    self.t_b_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    print("\t\tCONTADOR\t", self.cont)
                    print(self.quadruple)
                    self.size_stack_push(0)


    def create_exp_quadruple(self, type_exp):
        # print(self.pOperands, "operando")
        # print(self.pOperators, "operador")
        # print(self.pTypes, "tipo")
        # print(self.pJumps, "salto")

        #CORRECCION Se checa si se tienen operandos en la pila, esto solo sirve para 
        #resolver los operandos de comparacion 
        if (len(self.pOperators) != 0):
            #print("TAMA;O ES DIFERENTE DE 0")
            operator = self.pOperators[-1]
        else:
            #print("TAMA;O ES IGUAL A 0")
            operator = 0
        #print("OPERATOR",type_exp)
        match type_exp:
            #AND
            
            case 9:
                #print("ENTRO AL AND")
                if (operator == 9):
                    #LLAMAR LA FUNCIÓN PARA CREAR EL CUADRUPLO
                    print('&&')
                    self.inner_quad_exp()
            #OR
            case 10:
                if (operator == 10):
                    print('||')
                    self.inner_quad_exp()
            # + -
            case 11 | 12:
                if (operator == 11 or operator == 12):
                    print('+ -')
                    self.inner_quad_exp()
            # * / %
            case 13 | 14 | 15:
                if (operator == 13 or operator == 14 or operator == 15):
                    print('* / %')
                    self.inner_quad_exp()
            # ^
            case 16:
                if (operator == 16):
                    
                    print('^')
                    self.inner_quad_exp()
            # < > == !=
            case 20 | 22 | 23 | 24 | 31 | 32:
                if (operator == 20 or operator == 22 or operator == 23 or operator == 24 or operator == 31 or operator == 32):
                    print('< > == != <= >=')
                    print("ENTRO", self.pOperators)
                    self.inner_quad_exp()

        

    def insert_goto(self, goto_Type, func = None):
        # 1 -> gotofalso 18 | 2 -> gotverdadero  19| 3 -> GOTO 17
        print("PILA DE OPERANDOS", self.pOperands)
        print("PILA DE TIPOS", self.pTypes)
        
        #CORRECCION: SE AGREGO "CONDITION" PARA QUE LOS CUADRUPLOS DE GOTO TENGAN UNA CONDICION
        #EN EL CASO DE GOTO SIMPLE NO SE TIENE UNA CONDICION POR LO CUAL NO SE AGREGA NADA
        
        match goto_Type:

            #GOTOMAIN
            case 16:           
                self.quadruple.append([17,'','' , ''])
                self.cont += 1
                self.jump_stack_push()
                
            #GOTO
            case 17:
                #ANOTACIONES: POR EL MOMENTO SOLO ESTA PENSADO PARA EL IF
                print("ENTRO AL GOTO", self.cont)
                print ("PILA DE JUMPS", self.pJumps)
                false = self.jump_stack_pop()
                # save where i am for got to
                self.pJumps.append(self.cont-1)
                self.quadruple.append([17,'','' , ''])
                self.cont += 1
                self.fill(false, self.cont)
                

                print("\t\tCONTADOR\t", self.cont)
                print(self.quadruple)

            #GOTOF
            case 18:
                self.check_bool()
                condition = self.operands_stack_pop()
                self.type_stack_pop()
                self.size_stack_pop()
                
                self.quadruple.append([18,condition,'' , ''])
                self.cont += 1
                print("\t\tCONTADOR\t", self.cont)
                print(self.quadruple)
                #self.operators_stack_pop()
               

            #____GOTOV___
            case 19:
                self.check_bool()
                print("semilla", self.pJumps)
                gotoVerdadero = self.pJumps.pop()
                condition = self.operands_stack_pop()
                self.type_stack_pop()
                self.size_stack_pop()
                self.quadruple.append([19,condition,'' , ''])
                print("\tCONTADOR ", self.cont, "\nSIZE QUAD", len(self.quadruple))
                self.fill(self.cont - 1 , gotoVerdadero)
                self.cont += 1
                print("\t\tCONTADOR\t", self.cont)
                print('A DONDE RELLENAR', gotoVerdadero )

            #_________GOSUB____
            case 36:
                self.quadruple.append([36,'','' ,func])
                self.cont += 1

            #_________GOSPECIAL_______
            case 38:
                self.quadruple.append([38,'','',func])
                self.cont += 1


    def create_era(self,resources):
        print("ESTOY EN EL ERA")
        era_int = resources[0]
        era_float = resources[1] 
        era_bool = resources[2] 
        era_char = resources[3]
        era_df = resources[4]
        era_t_int = resources[5]
        era_t_float = resources[6] 
        era_t_bool = resources[7] 
        era_t_char = resources[8]
        era_t_df = resources[9]
        era_t_tp = resources[10]

        self.quadruple.append([35,'', era_int, era_t_int])
        self.cont += 1
        self.quadruple.append([35,'',era_float,era_t_float ])
        self.cont += 1
        self.quadruple.append([35,'', era_bool, era_t_bool])
        self.cont += 1
        self.quadruple.append([35,'',era_char, era_t_char])
        self.cont += 1
        self.quadruple.append([35,'',era_df, era_t_df])
        self.cont += 1
        self.quadruple.append([35,'',0, era_t_tp])
        self.cont += 1


        
        self.param_cont = 1
    
    def return_quad(self,return_type, function_place = None):
        #CHECK 
        print("return cuadruplo, ", self.pOperands)
        exp = self.operands_stack_pop()
        exp_type = self.type_stack_pop()
        func_type = oracle.datalor_translator(return_type.upper())
        size_exp = self.size_stack_pop()

        if(size_exp !=0):
            print("ERROR: ONLY ATOMIC VALUES ARE ALLOWED FOR RETURN")
            exit()

        if(exp_type == func_type):
            self.quadruple.append([33, exp,'', function_place])
            self.cont+=1
        else:
            print("ERROR: No match in return type")
            exit()

    def end_func_quad(self):
        self.quadruple.append([34, '','', ''])
        self.cont+=1
    
    def print_quadruple(self):
        printvalue = self.operands_stack_pop()
        tipo = self.type_stack_pop()
        
        size_print = self.size_stack_pop()
        row = 0
        col = 0
        if (size_print != 0):
            if(len(size_print)==4):
                #ARRAY
                row = size_print[1]
            if (len(size_print) == 2):
                #MATRIX
                row = size_print[0][1]
                col = size_print[1][2]

        self.quadruple.append([7, row,col, printvalue])
        
        self.cont+=1
        self.print_quadruples()
        
    # PREGUNTAR QUE SE HACE  CON EL READ 
    # SE TENÍA PENSADO USAR EL READ PARA EL TIPO LEER DATAFRAME
    #     
    def read_quadruple(self, value):
        #Create read quad
        address = self.t_df_cont + self.t_df_init
        if (self.t_df_cont > self.t_df_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_df_cont += 1
        
        self.quadruple.append([8, value,'', address])
        self.cont += 1

        #Insert read result 
        self.operands_stack_push(address)
        self.type_stack_push(5)
        self.size_stack_push(0)

        #self.quadruple.append()      
                    
    #         #SBER QUE TIPO ES EL RESULTANTE
    #         #INCREMENTAR EL CONTADOR ADECUADO
    #         #VERIFICAR QUE LOS TEMPORALES AÚN TENGAN ESPACIO
    #         #INSERTAR EN PILA DE OPERANDOS
    #         #CREAR EL CUADRUPLO


    # #def solve_expressions(self, precedencia):
    #    # print("")
    #     #if ()
    #     # si hay un operator en pila de operadores con la misma precedencia
    #     #     trae los valores a resolver
    #     #     preguntas al oraculo
    #     #       crea el cuadruplo
    #     #           darle la address temporal a la variable temp 
    #     #     type mistmatch

    #_________________<Array/Matrix>__________________
    def arr_mat_quad(self, size, curr_dim):
        #Check if type is integer
        self.check_integer()
        self.pTypes.pop()
        print("SIZE DOS", size)
        if (curr_dim == 1):
            #ARRAY
            if (len(size) == 4):
                print('ESTOY HACIENDO CUADRUPLOS DE ARRAY')
                s1 = self.operands_stack_pop()
                self.size_stack_pop()
                self.quadruple.append([39,s1,size[0],size[1]])
                self.cont += 1
                address = self.t_i_cont + self.t_i_init
                self.t_i_cont += 1
                #ADD (-K)
                self.quadruple.append([11,s1,size[2],address])
                self.cont += 1
                #ADD DIR BASE
                pointer = self.t_tp_cont + self.t_tp_init
                self.t_tp_cont += 1
                #Clear array dir_base
                dir_base = self.operands_stack_pop()
                self.size_stack_pop()
                self.quadruple.append([40,address,dir_base,pointer])
                self.cont += 1
                #Saves pointer in stack
                self.operands_stack_push(pointer)
                self.size_stack_push(0)

                
            #MATRIX
            if (len(size) == 2):
                print('ESTOY HACIENDO CUADRUPLOS DE MATRIX 1 ')

                s1 = self.operands_stack_pop()
                self.size_stack_pop()
                self.quadruple.append([39,s1,size[0][0],size[0][1]])
                self.cont += 1
                address = self.t_i_cont + self.t_i_init
                self.t_i_cont += 1
                #(S1*m1)
                m1 = size[0][2]
                self.quadruple.append([13,s1,m1,address])
                self.cont += 1    
                #Saves s1*m1 in stack
                self.operands_stack_push(address)
                self.type_stack_push(1)   
                self.size_stack_push(0)
        #MATRIX
        if (curr_dim == 2):
            print('ESTOY HACIENDO CUADRUPLOS DE MATRIX 2 ')

            s2 = self.operands_stack_pop()
            self.size_stack_pop()
            print("problema", size)
            self.quadruple.append([39,s2,size[1][0],size[1][1]])
            self.cont += 1
            #(S1*m1+S2)
            address = self.t_i_cont + self.t_i_init
            self.t_i_cont += 1
            s1m1 = self.operands_stack_pop()
            self.size_stack_pop()
            self.type_stack_pop()
            self.quadruple.append([11,s1m1,s2,address])
            self.cont += 1
            #ADD (-K)
            address2 = self.t_i_cont + self.t_i_init
            self.t_i_cont += 1
            self.quadruple.append([11,address,size[1][2],address2])
            self.cont += 1
            #ADD DIR BASE
            pointer = self.t_tp_cont + self.t_tp_init
            self.t_tp_cont += 1
            dir_base = self.operands_stack_pop()
            self.size_stack_pop()
            self.quadruple.append([40,address2,dir_base,pointer])
            self.cont += 1
            #ADD POINTER TO STACK
            self.operands_stack_push(pointer)
            self.size_stack_push(0)


    def print_poperands(self):
        
        self.print_quadruples()
        print ('OPERADORES',self.pOperators)
        print ('OPERANDOS',self.pOperands)
        print ('TIPOS',self.pTypes)
        print ('SIZEs', self.pSize)
        print ('SALTOS', self.pJumps)
        print ('CONTADOR', self.cont)
        

    def get_quad(self):
        return self.quadruple

    def print_quadruples(self):
        for i in range(len(self.quadruple)):
            print(i + 1 , " - ",self.quadruple[i])


