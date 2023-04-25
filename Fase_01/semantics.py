# ------------------------------------------------------------
# DATALOR: CHECKING FOR CONGRUENCE
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# semantics.... 
# ------------------------------------------------------------

semantics = {
    'int': {
        'int': {
            '+': 'int',
            '-': 'int',
            '*': 'int',
            '/': 'int',
            '%': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'int',
            '^': 'int'
            },
        'float': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            '%': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'float',
            '^': 'float'
        }
    },
    'float': {
        'float': {
            '+': 'float',
            '-': 'float',
            '*': 'float',
            '/': 'float',
            '%': 'float',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '!=': 'bool',
            '=': 'float',
            '^': 'float'
            }
    },
    'char': {
        'char': {
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '!=': 'bool'
        }
    },
    'bool': {
        'bool': {
            '&&': 'bool',
            '||': 'bool',
            '<': 'bool',
            '>': 'bool',
            '==': 'bool',
            '!=': 'bool'
        }
    }

}