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
        #print("MEMORY MAP", resources)
        int = [None] * resources[0]
        float = [None] * resources[1]
        char= [None] * resources[2]
        bool = [None] * resources[3]
        df = [None] * resources[4]

        t_int = [None] * resources[5]
        t_float = [None] * resources[6]
        t_char= [None] * resources[7]
        t_bool = [None] * resources[8]
        t_df = [None] * resources[9]
        t_pt = [None] * resources[10]

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
            print("GET INT", self.int[index])
            return self.int[index]
        
        #Global/Local Float
        if (tipo == 1):
            print("GET FLOAT", self.float[index])
            return self.float[index]
        
        #Global/Local Char
        if (tipo == 2):
            return self.char[index]
        
        #Global/Local Char
        if (tipo == 4):
            return self.df[index]
        
        #_____TEMPORAL____
        # TEMP INT
        if (tipo == 5):
            return self.t_int[index]

        #TEMPORAL FLOAT
        if (tipo == 6):
            return self.t_float[index]

        #TEMPORAL CHAR
        if (tipo == 7):
            return self.t_char[index]
    
        # TEMP BOOL
        if (tipo == 8):
            return self.t_bool[index]
        
        #TEMPORAL DATAFRAME
        if (tipo == 9):
            return self.t_df[index]
       
        #__________POINTER _______
        if(tipo == 10):
            #print("VALOR EN POINTER",self.pointer[index])
            return self.pointer[index]
       
       #_______CONSTANTES__________
        #Const int
        if(tipo == 11):
            return self.c_int[index]
       
        #Const Float
        if(tipo == 12):
            return self.c_float[index]
    
        #Const char
        if(tipo == 13):
            return self.c_char[index]
        
        
        

    def set_value(self, aux, value):
        tipo = aux[0]
        index = aux[1]
        print("SET VALUE", tipo, index, value)
        #________________GLOBAL/LOCAL_______
        #Int
        if (tipo == 0):
            self.int[index] = value
            
        # FLOAT
        if(tipo == 1):
            self.float[index] = value

        # CHAR
        if(tipo == 2):
            self.char[index] = value

         # DATAFRAME
        if(tipo == 4):
            self.df[index] = value


        #_______________TEMPORAL________________
        #INT
        if (tipo == 5):
            self.t_int[index] = value
        
        # FLOAT
        if (tipo == 6):
            self.t_float[index] = value
    
         #CHAR
        if (tipo == 7):
            self.t_char[index] = value

        #BOOL
        if (tipo == 8):
            self.t_bool[index] = value
        
        #DATAFRAME"
        if (tipo == 9):
            print("MIERCOLES val", index)
            self.t_df[index] = value
        
        #POINTER
        if (tipo == 10):
            self.pointer[index] = value

    def release_memory(self,size):

        if(size[0] != 0):
            self.int = self.int[:-size[0]]
        #print("RM INT AF", self.int)
        if(size[1] != 0):
            self.float = self.float[:-size[1]]
        #print("RM FLOAT AF", self.float)
        if(size[2] != 0):
            self.char = self.char[:-size[2]]
        if(size[3] != 0): 
        #print("RM BOOL BEF", self.bool)
            self.bool = self.bool[:-size[3]]
        #print("RM BOOL AF", self.bool)
        if(size[4] != 0):
            self.df = self.df[:-size[4]]
        if(size[5] != 0):
            self.t_int = self.t_int[:-size[5]]
        if(size[6] != 0):
            self.t_float = self.t_float[:-size[6]]
        
        if(size[7] != 0):
            self.t_char = self.t_char[:-size[7]]
        if(size[8] != 0):
            self.t_bool = self.t_bool[:-size[8]]
        if(size[9] != 0):
            self.t_df = self.t_df[:-size[9]]
        if(size[10] != 0):
            self.pointer = self.pointer[:-size[10]]
        

        
