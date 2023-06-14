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

        self.param_cont = 0
   
   #_________________STACKS__________________
   #_________________Setters/Getters_________________
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
    
    def jump_stack_pop(self):
        return self.pJumps.pop()
    
    def jump_seed(self):
        self.pJumps.append(self.cont)
    
    #CONT PLACE
    def cont_place(self):
        return self.cont

    #False bottom
    def false_button(self):
        self.pOperators.append('(')
    
    #Relase false bottom
    def release_false_button(self):
        if (len(self.pOperators) != 0):
            if(self.pOperators[-1] == '('):
                self.pOperators.pop()

    #FILL
    #Fills the quadruple with the jump
    #Recieves the jump and the place
    def fill(self, jump, place):
        self.quadruple[jump][3] = place

    #<FOR> Control and final variables declaration

    def control_var(self ):
        self.check_integer()
        exp_type = self.type_stack_pop()
        exp = self.operands_stack_pop()
        self.size_stack_pop()
        #Generates a control variable and its type
        vControl = self.pOperands[-1]
        control_type = self.pTypes[-1]
        #Creates a place to save the control variable
        place = self.t_i_cont + self.t_i_init
        if (self.t_i_cont > self.t_i_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_i_cont += 1
        
        #Check for type mismatch
        res = oracle.oracle_cmddwtm(str(exp_type),str(control_type),'21')
        if (res != '1'):
            print("ERROR: TYPE MISMATCH")
            exit()
        else:
            #Generates a quadruple for the value assisgnment to the control variable
            self.quadruple.append([21, exp, '', vControl])
            self.cont += 1
            #Generates a quadruple for the assignment of the control variable
            self.quadruple.append([21, vControl, '', place])
            self.cont += 1
            #Pushes the control variable to the operands stack
            self.operands_stack_push(place)
            self.size_stack_push(0)
            self.type_stack_push(control_type)
            


    def final_var(self):
        self.check_integer()
        exp_type = self.type_stack_pop()
        exp = self.operands_stack_pop()
        self.size_stack_pop()
        #Generates a place for final variable 
        place = self.t_i_cont + self.t_i_init
        if (self.t_i_cont > self.t_i_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_i_cont += 1
        igual = self.operators_stack_pop()
        self.quadruple.append([21, exp, '', place])
        self.cont += 1
        self.operands_stack_push(place)
        self.type_stack_push(exp_type)
        self.size_stack_push(0)

        #Duplicate data for control variable and final variable
        #So it wont lose once the operation is done
        vcontrol = self.pOperands[-2]
        control_type = self.pTypes[-2]
        self.operands_stack_push(vcontrol)
        self.type_stack_push(control_type)
        self.size_stack_push(0)


    #Create the quadruples for increasing  the control variable
    #and fill the jump for the condition
    def end_for(self):
        vControl = self.operands_stack_pop()
        vControl_type = self.type_stack_pop()
        self.size_stack_pop()
        #A place is generated for the increment of the control variable
        place = self.t_i_cont + self.t_i_init
        if (self.t_i_cont > self.t_i_size):
            print("ERROR: STACK OVERFLOW")
            exit()
        self.t_i_cont += 1
        #Get the place where the value of the control variable was stored
        idfrom = self.operands_stack_pop()
        idfrom_type = self.type_stack_pop()
        self.size_stack_pop()
        #25000 because is the place where 1 is stored
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

    #Functions to check each type at validation
    #_________________CHECKERS______________________#
                
    def check_bool(self):
        if(self.pTypes[-1] != '4'):
            print('Bool type was expected')
            exit()
            
    def check_integer(self):
        if(int(self.pTypes[-1]) != 1):
             print('Integer type was expected')
             exit()

    def check_const(self):
        if(self.pTypes[-1] != '28'):
            print('Constant Integer type was expected')
            exit()

    #Function to resolve EXP for queadruples 

    #_________________________ASSIGN__________________#
    def assign_quadruple(self):
       #POP from the tables for assigning it to the quadruple
        operator = self.operators_stack_pop()
        operandR = self.operands_stack_pop()
        size_opR = self.size_stack_pop()
        result = self.operands_stack_pop()
        size_result = self.size_stack_pop()
        if(size_opR != 0 or size_result !=0 and size_opR != None):
            print("ERROR: ONLY ATOMIC ASSIGNS ARE ALLOWED")
            exit()


        #POP to the types
        typeR = self.type_stack_pop()
        typeRes = self.type_stack_pop()
        #ASK THE ORACLE IF MDDWTM

        oracle_answer = oracle.oracle_cmddwtm(str(typeRes),str(typeR),str(operator))
        #CREATING THE CUADRUPLE
        self.quadruple.append([operator, operandR,'',result])
        self.cont += 1
        

    #FUNCTION FOR ASSIGNING THE VARIABLES THAT ARE GOING TO BE PASSED TO THE QUADRUPLE 
    def inner_quad_exp(self):
        operandR = self.operands_stack_pop()
        size_right = self.size_stack_pop()

        typeR = self.type_stack_pop()
       
        operandL = self.operands_stack_pop()
        size_left = self.size_stack_pop()
        typeL = self.type_stack_pop()
        
        operator = self.operators_stack_pop()
        size = 0
        #ASK TO THE ORACLE
        type_result = oracle.oracle_cmddwtm(str(typeL),str(typeR),str(operator))
        self.pTypes.append(type_result)

        #ASK SIZE
        #Both are variables
        
        if(size_right != 0 or size_left != 0):
            print("ERROR: ONLY ATOMIC SIZES ARE AVAILABLE FOR EXPRESSIONS ")
            exit()
 
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
                    self.size_stack_push(0)

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
                    self.size_stack_push(0)

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
                    self.size_stack_push(0)

            #BOOLEAN
            case '4':
                if (self.t_b_cont > self.t_b_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_b_init + self.t_b_cont
                    self.t_b_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    self.size_stack_push(0)


    #Creates the call for each type of expresion and its priority
    def create_exp_quadruple(self, type_exp):
    
        if (len(self.pOperators) != 0):
            operator = self.pOperators[-1]
        else:
            operator = 0
        match type_exp:
            #AND
            
            case 9:
                if (operator == 9):
                    self.inner_quad_exp()
            #OR
            case 10:
                if (operator == 10):
                    self.inner_quad_exp()
            # + -
            case 11 | 12:
                if (operator == 11 or operator == 12):
                    self.inner_quad_exp()
            # * / %
            case 13 | 14 | 15:
                if (operator == 13 or operator == 14 or operator == 15):
                    self.inner_quad_exp()
            # ^
            case 16:
                if (operator == 16):
                    
                    self.inner_quad_exp()
            # < > == !=
            case 20 | 22 | 23 | 24 | 31 | 32:
                if (operator == 20 or operator == 22 or operator == 23 or operator == 24 or operator == 31 or operator == 32):
                    self.inner_quad_exp()

        

    def insert_goto(self, goto_Type, func = None):
        # 1 -> gotofalso 18 | 2 -> gotverdadero  19| 3 -> GOTO 17
        
        
        match goto_Type:

            #GOTOMAIN
            case 16:           
                self.quadruple.append([17,'','' , ''])
                self.cont += 1
                self.jump_stack_push()
                
            #GOTO
            case 17:
                false = self.jump_stack_pop()
                # save where i am for got to
                self.pJumps.append(self.cont-1)
                self.quadruple.append([17,'','' , ''])
                self.cont += 1
                self.fill(false, self.cont)

            #GOTOF
            case 18:
                self.check_bool()
                condition = self.operands_stack_pop()
                self.type_stack_pop()
                self.size_stack_pop()
                
                self.quadruple.append([18,condition,'' , ''])
                self.cont += 1
                #self.operators_stack_pop()

            #____GOTOV___
            case 19:
                self.check_bool()
                gotoVerdadero = self.pJumps.pop()
                condition = self.operands_stack_pop()
                self.type_stack_pop()
                self.size_stack_pop()
                self.quadruple.append([19,condition,'' , ''])
                self.fill(self.cont - 1 , gotoVerdadero)
                self.cont += 1

            #_________GOSUB____
            case 36:
                self.quadruple.append([36,'','' ,func])
                self.cont += 1

            #_________GOSPECIAL_______
            case 38:
                self.quadruple.append([38,'','',func])
                self.cont += 1


    #Creates the cuadruples for ERA and start params count
    def create_era(self,resources):
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
    
    #Creates the cuadruples and avoid it to return not atomic values 
    def return_quad(self,return_type, function_place = None):
        #CHECK 
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

    #Creates the cuadruples for the end of a function
    def end_func_quad(self):
        self.quadruple.append([34, '','', ''])
        self.cont+=1
    
    #Creates a for print quadruple
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
        
    def get_address(self, tipo):
        if (tipo == 1):
            a = self.t_i_cont + self.t_i_init
            self.t_i_cont += 1
            return a
        elif (tipo == 2):
            a = self.t_f_cont + self.t_f_init
            self.t_f_cont += 1
            return a
        elif (tipo == 4):
            a = self.t_c_cont + self.t_c_init
            self.t_c_cont += 1
            return a
        elif (tipo == 5):
            a = self.t_df_cont + self.t_df_init
            self.t_df_cont += 1
            return a
        
    
    #Creates a for read quadruple
    def read_quadruple(self, value):
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


    #_________________<Array/Matrix>__________________
    def arr_mat_quad(self, size, curr_dim):
        #Check if type is integer
        self.check_integer()
        self.pTypes.pop()
        if (curr_dim == 1):
            #ARRAY
            if (len(size) == 4):
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

            s2 = self.operands_stack_pop()
            self.size_stack_pop()
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

    #Function for print stacks, only for debugging purposes
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
    
    #Function for print quad, only for debugging purposes
    def print_quadruples(self):
        for i in range(len(self.quadruple)):
            print(i + 1 , " - ",self.quadruple[i])


