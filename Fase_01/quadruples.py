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
        
        #self.temp_cont = {} 
   
   #_________________STACKS__________________

    #Function for opertors stack
    def operators_stack_push(self,operator):
        self.pOperators.append(operator)

    def operators_stack_pop(self):
        self.pOperators.pop()

    #Function for operands stack
    def operands_stack_push(self,operand):
        self.pOperands.append(operand)

    def operands_stack_pop(self):
        self.pOperands.pop()

    #TYPE STACK
    def type_stack_push(self,type):
        self.pTypes.append(type)

    def type_stack_pop(self):
        self.pTypes.pop()

    #Function for creating quadruples
    def create_quadruple(self, operator, operandR, result = None, operandL = None):
        #CHECK SEMANTICS
        operator = oracle.datalor_translator(operator)
        operandR = oracle.datalor_translator()
        result = oracle.datalor_dictionary(result)
        operandL = oracle.datalor_translator(operandL)


        #oracle.semantics

    def solve_expressions(self, precedencia):
        print("")
        #if ()
        # si hay un operator en pila de operadores con la misma precedencia
        #     trae los valores a resolver
        #     preguntas al oraculo
        #       crea el cuadruplo
        #           darle la address temporal a la variable temp 
        #     type mistmatch