# -----------------------------------------------------------
# DATALOR: Virtual Machine
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# Virtual Machine....
# -----------------------------------------------------------
from memory_map import MemoryMap

mp = MemoryMap()

class VirtualMachine:
    
    def __init__(self) :
      
        self.quaduples = []
        self.resources = []
        self.const = {}
        #Value ranges
        #GLOBALES
        self.g_i_init = 1000
        self.g_f_init = 3000
        self.g_c_init = 5000
        self.g_df_init = 7000

        #LOCALES
        self.l_i_init = 9000
        self.l_f_init = 11000
        self.l_c_init = 13000
        self.l_df_init = 15000

        #START TEMPORALES
        self.t_i_init = 17000
        self.t_f_init = 19000
        self.t_c_init = 21000
        self.t_b_init = 23000
        self.t_df_init = 31000
        
        #CONSTANTES
        self.c_i_init = 25000
        self.c_f_init = 27000
        self.c_c_init = 29000

        
        self.t_tp_init = 33000
       
       
    
    def set_quadruples(self, quad):
        self.quaduples = quad
        print("SET QUAD", self.quaduples)

    def set_resources (self, res):
        self.resources = res
        print("SET RES", self.resources)
    
    def set_const (self, const):
        self.const = const
        print("SET CONST", const)


    def start_vm(self):
        print("________VIRTUAL MACHINE__________")
        print("QUAD:\n ", self.quaduples)
        print("\n RES: ",self.resources)
        print("\n CONST: ",self.const)
        #print(mp.res_global(self.resources[0]))
        main_offset = mp.res_global(self.resources[0])
        print("MAIN OFFSET", main_offset)
        end_main = mp.res_global(self.resources[1])
        print("END MAIN", end_main)
        self.sort_const()
        

        print("________MEMORY MAP__________")
        print(  mp.int,     ("\n"),
                mp.float,("\n"),
                mp.char,("\n"),
                mp.bool, ("\n"),
                mp.df,("\n"),
                mp.t_int,("\n"),
                mp.t_float,("\n"),
                mp.t_char,("\n"),
                mp.t_bool,("\n"),
                mp.t_df,("\n"),
                mp.pointer, ("\n"),
                mp.c_int, ("\n"),
                mp.c_float, ("\n"),
                mp.c_char,("\n"),
                )
        

    def real_address(self, offset, virtual_address):
        #________GLOBAL_________
        #INT
        if(virtual_address >= self.g_i_init and virtual_address < self.g_f_init):
            address = (virtual_address - 1000)
            return [0,address]
       
       #FLOAT
        if(virtual_address >= self.g_f_init and virtual_address < self.g_c_init):
            address = (virtual_address - 3000)
            return [1,address]
        
        #CHAR
        if(virtual_address >= self.g_c_init and virtual_address < self.g_df_init):
            address = (virtual_address - 5000)
            return [3,address]
        
        #DATAFRAME
        if(virtual_address >= self.g_df_init and virtual_address < self.l_i_init):
            address = (virtual_address - 7000)
            return [4,address]
        
         #________LOCALES________
       #INT
        if(virtual_address >= self.l_i_init and virtual_address < self.l_f_init):
            address = (virtual_address - self.l_i_init + offset[0])
            return [0,address]
       
       #FLOAT
        if(virtual_address >= self.l_f_init and virtual_address < self.l_c_init):
            address = (virtual_address - self.l_f_init + offset[1])
            return [1,address]
        
        #CHAR
        if(virtual_address >= self.l_c_init and virtual_address < self.l_df_init):
            address = (virtual_address - self.l_c_init + offset[3])
            return [3,address]
        
        #DATAFRAME
        if(virtual_address >= self.l_df_init and virtual_address < self.t_i_init):
            address = (virtual_address - self.l_df_init + offset[4])
            return [4,address]
        
         #________TEMPORALES________
       #INT
        if(virtual_address >= self.t_i_init and virtual_address < self.t_f_init):
            address = (virtual_address - self.t_i_init + offset[5])
            return [0,address]
       
       #FLOAT
        if(virtual_address >= self.t_f_init and virtual_address < self.t_c_init):
            address = (virtual_address - self.t_f_init + offset[6])
            return [1,address]
        
        #BOOL
        if(virtual_address >= self.t_b_init and virtual_address < self.t_df_init):
            address = (virtual_address - self.t_b_init + offset[7])
            return [2,address]
        
        #CHAR
        if(virtual_address >= self.t_c_init and virtual_address < self.t_b_init):
            address = (virtual_address - self.t_c_init + offset[8])
            return [3,address]
        
        #DATAFRAME
        if(virtual_address >= self.t_df_init and virtual_address < self.c_i_init):
            address = (virtual_address - self.t_df_init + offset[9])
            return [4,address]

        #________CONSTANTES________

    def sort_const(self):
        # const_value =  list(self.const.keys)
        # const_address = list(self.const)

       
        const_value = []
        int_list = []
        float_list = []
        char_list = []
        const_value = list(self.const.keys())

        print( "Const", const_value)
        for i in range(len(const_value)):
            print(type(const_value[i]).__name__)
            
            if ((type(const_value[i]).__name__) == 'int'):
                int_list.append(const_value[i])
            
            if ((type(const_value[i]).__name__) == 'float'):
                float_list.append(const_value[i])
            
            if ((type(const_value[i]).__name__) == 'str'):
                char_list.append(const_value[i])

        mp.set_constants([int_list, float_list, char_list])
        
    def vm_handler(self, inst_pointer):
        operation = self.quaduples[inst_pointer][0]
        
        match operation:

            #GOTO
            case 17:
                ip = self.quaduples[inst_pointer][3]
                self.vm_handler(ip)
            
            #PLUS
            case 11:
                #Borrar
                exit()
