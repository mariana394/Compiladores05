# -----------------------------------------------------------
# DATALOR: CUADRUPLOS
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# 
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
        self.pTypes = [] 

        #_____________TEMPORAL VARIABLES____________#
        #TEMPORALES
        self.t_i_size = 1999
        self.t_f_size = 1999
        self.t_c_size = 1999
        self.t_b_size = 1999

        #START TEMPORALES
        self.t_i_init = 17000
        self.t_f_init = 19000
        self.t_c_init = 21000
        self.t_b_init = 23000

        #COUNTER TEMPORALES
        self.t_i_cont = 0
        self.t_f_cont = 0
        self.t_c_cont = 0
        self.t_b_cont = 0 

        #self.temp_cont = {} 
   
   #_________________STACKS__________________

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

    #FONDO FALSO 
    def false_button(self):
        self.pOperators.append('(')
        print('fondo falso',self.pOperators)
    
    def release_false_button(self):
        print('release fondo falso',self.pOperators)
        if (len(self.pOperators) != 0):
            if(self.pOperators[-1] == '('):
                self.pOperators.pop()


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


    #Function to resolve EXP for queadruples 

    #_________________________ASSIGN__________________#
    def assign_quadruple(self):
        #print(self.pOperators, self.pOperands)
       #POP from the tables for assigning it to the quadruple
        operator = self.operators_stack_pop()
        operandR = self.operands_stack_pop()
        result = self.operands_stack_pop()
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
        print(self.quadruple)

    #__________________EXPRESSIONS QUADRUPLES________________________
     
    # def power_quadruple(self):
    #     operator = self.pOperators[-1]
    #     if(operator == 16):
    #         operandR = self.operands_stack_pop()
    #         typeR = self.type_stack_pop()
    #         operandL = self.operands_stack_pop()
    #         typeL = self.type_stack_pop()
    #         operator = self.operators_stack_pop()
            
    #         #ASK TO THE ORACLE
    #         type_result = oracle.oracle_cmddwtm(str(typeL)),str(typeR,str(operator))
    #         self.pTypes.append(type_result)
    #         match type_result:
    #             #INTEGER
    #             case 1:
    #                 if (self.t_i_cont > self.t_i_size):
    #                     print("ERROR: STACK OVERFLOW")
    #                     exit()
    #                 else:
    #                     result = self.t_i_init + self.t_i_cont
    #                     self.quadruple.append([operator, operandL, operandR, result])
    #                     self.cont += 1
    #                     self.operands_stack_push(result)
    #             #FLOAT
    #             case 2:
    #                 self.t_f_cont += 1
    #                 if (self.t_f_cont > self.t_f_size):
    #                     print("ERROR: STACK OVERFLOW")
    #                     exit()
    #                 else:
    #                     result = self.t_f_init + self.t_f_cont
    #                     self.quadruple.append([operator, operandL, operandR, result])
    #                     self.cont += 1
    #
    #                      self.operands_stack_push(result)

    #FUNCTION FOR ASSIGNING THE VARIABLES THAT ARE GOING TO BE PASSED TO THE QUADRUPLE 
    def inner_quad_exp(self):
        operandR = self.operands_stack_pop()
        typeR = self.type_stack_pop()
        operandL = self.operands_stack_pop()
        typeL = self.type_stack_pop()
        operator = self.operators_stack_pop()
        
        #ASK TO THE ORACLE
        print('operator', operator)
        type_result = oracle.oracle_cmddwtm(str(typeL),str(typeR),str(operator))
        self.pTypes.append(type_result)
        match type_result:
            #INTEGER
            case '1':
                if (self.t_i_cont > self.t_i_size):
                    #print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_i_init + self.t_i_cont
                    self.t_i_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    #print ('OPERANDOS',self.pOperands)
            #FLOAT
            case '2':
                self.t_f_cont += 1
                if (self.t_f_cont > self.t_f_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_f_init + self.t_f_cont
                    self.t_f_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    #print ('OPERANDOS',self.pOperands)
            #CHAR
            case '3':
                self.t_c_cont += 1
                if (self.t_c_cont > self.t_c_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_c_init + self.t_c_cont
                    self.t_c_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    #print ('OPERANDOS',self.pOperands)
            #BOOLEAN
            case '4':
                self.t_b_cont += 1
                if (self.t_b_cont > self.t_b_size):
                    print("ERROR: STACK OVERFLOW")
                    exit()
                else:
                    result = self.t_b_init + self.t_b_cont
                    self.t_b_cont += 1
                    self.quadruple.append([operator, operandL, operandR, result])
                    self.cont += 1
                    self.operands_stack_push(result)
                    #print ('OPERANDOS',self.pOperands)


    def create_exp_quadruple(self, type_exp):
        print(self.pOperands, "operando")
        print(self.pOperators, "operador")

        operator = self.pOperators[-1]

        #print("OPERATOR",type_exp)
        match type_exp:
            #AND
            case 9:
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
            case 20 | 22 | 23 | 24:
                if (operator == 20 or operator == 22 or operator == 23 or operator == 24):
                    print('< > == !=')
                    self.inner_quad_exp()
            
    def check_bool(self):
        if(self.pTypes[- 1] != 4):
            print('Bool type was expected')
            exit()
            

    def insert_goto(self, goto_Type):
        # 1 -> gotofalso 18 | 2 -> gotverdadero  19| 3 -> GOTO 17

        self.check_bool()
        match goto_Type:

            case 17:
                self.quadruple.append([17,'','' , ''])
                self.cont += 1

            case 18:
                self.quadruple.append([18,'','' , ''])
                self.cont += 1

            case 19:
                self.quadruple.append([19,'','' , ''])
                self.cont += 1

          
                    
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

    def print_poperands(self):
        print ('OPERANDOS',self.pOperands)