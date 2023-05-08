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
        self.index_temp = 1
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
        self.index_temp = 0

    #_________________________ASSIGN__________________#
    def assign_quadruple(self):
        #print(self.pOperators, self.pOperands)
       #POP from the tables for assigning it to the quadruple
        operator = self.operators_stack_pop()
        operandR = self.operands_stack_pop()
        result = self.operands_stack_pop()
       #POP to the types
        #print(self.pTypes)
        typeD = self.type_stack_pop()
        typeRes = self.type_stack_pop()
        #ASK THE ORACLE IF MDDWTM
        oracle_answer = oracle.oracle_cmddwtm(str(typeRes),str(typeD),str(operator))
        print("Oracle answer",oracle_answer)
       #CREATING THE CUADRUPLE
        self.quadruple.append([operator, operandR,'',result])
        print(self.quadruple)

    #def solve_expressions(self, precedencia):
       # print("")
        #if ()
        # si hay un operator en pila de operadores con la misma precedencia
        #     trae los valores a resolver
        #     preguntas al oraculo
        #       crea el cuadruplo
        #           darle la address temporal a la variable temp 
        #     type mistmatch