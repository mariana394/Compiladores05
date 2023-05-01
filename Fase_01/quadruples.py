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
        
        #self.temp_cont = {} 
    
    #Function for creating quadruples
    def create_quadruple(self, operator, operandL, result, operandR = None):
        #CHECK SEMANTICS
        operator = oracle.datalor_translator(operator)
        
        #oracle.semantics

    def solve_expressions(self, precedencia):
        if ()
        # si hay un operator en pila de operadores con la misma precedencia
        #     trae los valores a resolver
        #     preguntas al oraculo
        #       crea el cuadruplo
        #           darle la address temporal a la variable temp 
        #     type mistmatch
        