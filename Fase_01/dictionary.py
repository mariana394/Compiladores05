# ------------------------------------------------------------
# DATALOR: DICTIONARY
# Mariana Favarony Avila - A01704671
# Mario Juarez - A01411049
# Keys to every token in the language
# ------------------------------------------------------------

class Dictionary:
    
    def __init__(self):
        self.datalor_dictionary = {
            #TIPOS SIMPLE
            'INT' : 1,
            'FLOAT': 2,
            'CHAR' : 3,
            'BOOL' : 4,

            #TIPOS COMPUESTOS
            'DATE' : 5,
            'DATAFRAME' : 6,

            #PALABRAS RESERVADAS
            'PRINT': 7,
            'READ': 8,
            
            #OPERADORES LOGICOS
            'AND':9,
            'OR':10,

            #OPERADORES
            'PLUS':11,
            'MINUS':12,
            'MULTIPLY':13,
            'DIVIDE':14,
            'MODULE':15,
            'POWER':16,

            #GOTOS CONDICIONALES-CICLOS
            'GOTO' : 17,
            'GOTOF': 18,
            'GOTOV': 19,

            #EXPRESSIONS
            'EQUAL': 20, #==
            'ASSIGN': 21, #=
            'GTHAN': 22,
            'LTHAN': 23,
            'NOTEQUAL': 24, #!=
            'COLON': 25,
            'SEMICOLON': 26,
            'COMMA': 27,               

            #CONST
            'CTE_INT' : 28,
            'CTE_FLOAT': 29,
            'CTE_CHAR': 30 
        }

        self.semantics = {
            '1': {
                '1': {
                    '11': '1',
                    '12': '1',
                    '13': '1',
                    '14': '1',
                    '15': '2',
                    '23': '4',
                    '22': '4',
                    '20': '4',
                    '24': '4',
                    '21': '1',
                    '16': '1'
                    },
                '2': {
                    '11': '2',
                    '12': '2',
                    '13': '2',
                    '14': '2',
                    '15': '2',
                    '23': '4',
                    '22': '4',
                    '20': '4',
                    '24': '4',
                    '21': '2',
                    '16': '2'
                }
            },
            '2': {
                '2': {
                    '11': '2',
                    '12': '2',
                    '13': '2',
                    '14': '2',
                    '15': '2',
                    '23': '4',
                    '22': '4',
                    '20': '4',
                    '24': '4',
                    '21': '2',
                    '16': '2'
                    }
            },
            '3': {
                '3': {
                    '23': '4',
                    '22': '4',
                    '20': '4',
                    '24': '4'
                }
            },
            '4': {
                '4': {
                    '9': '4',
                    '10': '4',
                    '23': '4',
                    '22': '4',
                    '20': '4',
                    '24': '4'
                }
            }
        }


    def datalor_translator(self, token):
        if token in self.datalor_dictionary.keys():
            return self.datalor_dictionary[token]
        else:
            print("UNDEFINED TOKEN", token)
            exit()
