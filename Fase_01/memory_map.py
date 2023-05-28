# ------------------------------------------------------------
# DATALOR: MEMORY MAP
# Mariana Favarony Avila - A01704671
# Mario Juarez - A01411049
# Memory map for the virtual machine
# ------------------------------------------------------------

class MemoryMap:

    def __init__(self):
        
        self.int = []
        self.float = []
        self.char= []
        self.bool = []
        self.df = []
        self.t_int = []
        self.t_float = []
        self.t_char= []
        self.t_bool = []
        self.t_df = []
        self.pointer = []
        self.c_int = []
        self.c_float = []
        self.c_char = []       
        self.overflow = 10000

        


    def res_global (self, resources):
        print("MEMORY MAP", resources)
        int = [0] * resources[0]
        float = [0] * resources[1]
        char= [0] * resources[2]
        bool = [0] * resources[3]
        df = [0] * resources[4]

        t_int = [0] * resources[5]
        t_float = [0] * resources[6]
        t_char= [0] * resources[7]
        t_bool = [0] * resources[8]
        t_df = [0] * resources[9]
        t_pt = [0] * resources[10]

        self.int += (int)
        self.float += (float)
        self.char += (char)
        self.bool += (bool)
        self.df += (df)
        #Temporales
        self.t_int += (t_int)
        self.t_float += (t_float)
        self.t_char += (t_char)
        self.t_bool += (t_bool)
        self.t_df += (t_df)
        self.pointer += (t_pt)

        self.check_stack_over_flow()

        seeds = [len(self.int), len(self.float),len(self.char), len(self.bool), len(self.df),
                 len(self.t_int), len(self.t_float), len(self.t_char), len(self.t_bool),len(self.t_df),
                 len(self.pointer)]
        
        return seeds

    def check_stack_over_flow(self):
        
        if(len(self.int) > self.overflow):
            print("ERROR: Stack overflow on Int variable")
            exit()
        
        if(len(self.float) > self.overflow):
            print("ERROR: Stack overflow on Float variable")
            exit()
            
        if(len(self.char) > self.overflow):
            print("ERROR: Stack overflow on char variable")
            exit()
            
        if(len(self.bool) > self.overflow):
            print("ERROR: Stack overflow on bool variable")
            exit()


        if(len(self.df) > self.overflow):
            print("ERROR: Stack overflow on dataframe variable")
            exit()
            
        #TEMPORALES
        if(len(self.t_int) > self.overflow):
            print("ERROR: Stack overflow")
            exit()

        if(len(self.t_float) > self.overflow):
            print("ERROR: Stack overflow")
            exit()

        if(len(self.t_bool) > self.overflow):
            print("ERROR: Stack overflow")
            exit()

        if(len(self.t_char) > self.overflow):
            print("ERROR: Stack overflow")
            exit()
            
        if(len(self.t_df) > self.overflow):
            print("ERROR: Stack overflow")
            exit()
            
        if (len(self.pointer) > self.overflow):
            print("ERROR: Stack overflow")
            exit()

    def set_constants(self,consts):
        self.c_int += consts[0]
        self.c_float += consts[1]
        self.c_char += consts[2]
    
    #_____________QUADRUPLES GETTERS/SETTERS_____________#

    def get_value(self,aux):
        tipo = aux[0]
        index = aux[1]

        #Global/Local Int
        if (tipo == 0):
            return self.int[index]
        
        #Global/Local Float
        if (tipo == 1):
            return self.float[index]
        
        #Global/Local Char
        if (tipo == 2):
            return self.char[index]
        
        #Global/Local Char
        if (tipo == 3):
            return self.df[index]
        
        #_____TEMPORAL____
        # TEMP INT
        if (tipo == 4):
            return self.t_int[index]

        #TEMPORAL FLOAT
        if (tipo == 5):
            return self.t_float[index]
       
       # TEMP BOOL
        if (tipo == 6):
            return self.t_bool[index]

        #TEMPORAL CHAR
        if (tipo == 7):
            return self.t_char[index]
        
        #TEMPORAL DATAFRAME
        if (tipo == 8):
            return self.t_df[index]
       
       
       #_______CONSTANTES__________
        #Const int
        if(tipo == 9):
            return self.c_int[index]
        
        #Const Float
        if(tipo == 10):
            return self.c_float[index]
    
        #Const char
        if(tipo == 11):
            return self.c_char[index]
        

    


    def set_value(self, aux, value):
        tipo = aux[0]
        index = aux[1]

        #GLOBAL/LOCAL FLOAT
        if(tipo == 1):
            self.float[index] = value

        #TEMPORAL FLOAT
        if (tipo == 5):
            self.t_float[index] = value
    
            