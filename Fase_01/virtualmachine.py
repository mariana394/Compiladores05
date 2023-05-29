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
        print("____________________________________________________________")

        self.vm_handler(0, main_offset, end_main)
        print("____________________________________________________________")

        
        
    def print_todo(self):

        print("________MEMORY MAP__________")
        print(  mp.int,     ("int \n"),
                mp.float,("float\n"),
                mp.char,("char\n"),
                mp.df,("df\n"),
                mp.t_int,("t_int\n"),
                mp.t_float,("t_float\n"),
                mp.t_char,("t_char\n"),
                mp.t_bool,("t_bool\n"),
                mp.t_df,("t_df\n"),
                mp.pointer, ("pointer\n"),
                mp.c_int, ("c_int\n"),
                mp.c_float, ("c_float\n"),
                mp.c_char,("c_char \n"),
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
            return [2,address]
        
        #DATAFRAME
        if(virtual_address >= self.g_df_init and virtual_address < self.l_i_init):
            address = (virtual_address - 7000)
            return [3,address]
        
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
            return [2,address]
        
        #DATAFRAME
        if(virtual_address >= self.l_df_init and virtual_address < self.t_i_init):
            address = (virtual_address - self.l_df_init + offset[4])
            return [3,address]
        
         #________TEMPORALES________
       #INT
        if(virtual_address >= self.t_i_init and virtual_address < self.t_f_init):
            address = (virtual_address - self.t_i_init + offset[5])
            return [4,address]
       
       #FLOAT
        if(virtual_address >= self.t_f_init and virtual_address < self.t_c_init):
            address = (virtual_address - self.t_f_init + offset[6])
            return [5,address]
        
        #BOOL
        if(virtual_address >= self.t_b_init and virtual_address < self.c_i_init):
            address = (virtual_address - self.t_b_init + offset[7])
            return [6,address]
        
        #CHAR
        if(virtual_address >= self.t_c_init and virtual_address < self.t_b_init):
            address = (virtual_address - self.t_c_init + offset[8])
            return [7,address]
        
        #DATAFRAME
        if(virtual_address >= self.t_df_init and virtual_address < self.t_tp_init):
            address = (virtual_address - self.t_df_init + offset[9])
            return [8,address]

        #________CONSTANTES________
        #INT
        if(virtual_address >= self.c_i_init and virtual_address < self.c_f_init):
            address = (virtual_address - self.c_i_init)
            #5 -> int Const
            return [9, address]
        
        #FLOAT
        if(virtual_address >= self.c_f_init and virtual_address < self.c_c_init):
            address = (virtual_address - self.c_f_init)
            #6 -> float Const
            return [10, address]
        
        #CHAR
        if(virtual_address >= self.c_c_init and virtual_address < self.t_df_init):
            address = (virtual_address - self.c_c_init)
            #7 -> char Const
            return [11, address]
        
        #__________POINTERS__________
        if(virtual_address >= self.t_tp_init and virtual_address < self.t_tp_init + 1999):
            address = (virtual_address - self.t_tp_init)
            return [12, address]

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
            #print(type(const_value[i]).__name__)
            
            if ((type(const_value[i]).__name__) == 'int'):
                int_list.append(const_value[i])
            
            if ((type(const_value[i]).__name__) == 'float'):
                float_list.append(const_value[i])
            
            if ((type(const_value[i]).__name__) == 'str'):
                char_list.append(const_value[i])

        mp.set_constants([int_list, float_list, char_list])
        
    def check_len_quad(self, inst_pointer):
        if(inst_pointer >= len(self.quaduples)):
            print("END OF FILE")
            self.print_todo()
            exit()

    def vm_handler(self, inst_pointer, offset, offset_end):
        operation = self.quaduples[inst_pointer][0]
        print("Curr_quad ", self.quaduples[inst_pointer] )
        match operation:

            #PRINT
            case 7:
                value_p = self.quaduples[inst_pointer][3]
                real_print_address =  self.real_address(offset, value_p)   
                print("PRINT ADD",real_print_address)
                print_v = mp.get_value(real_print_address)
                
                print(print_v)
                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
            
            #READ ->INCOMPLETO
            case 8:
                value_r = self.quaduples[inst_pointer][3]
                real_read_address =  self.real_address(offset, value_r)
                #Read a file in the same dir scope

            #AND
            case 9:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3]

                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)

                value = left_value and right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
                
                
            #OR
            case 10:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3]

                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)

                value = left_value or right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #PLUS - Sin terminar 
            case 11:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value + right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
                
            #MINUS
            case 12:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value - right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
            
            #MULTIPLY
            case 13:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 

                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)

                value = left_value * right_value
                mp.set_value(res_real_address,value)
                
                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
            
            #DIVIDE
            case 14:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value / right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #MODULE
            case 15:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value % right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #POWER
            case 16:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                #print("power", left_value, right_value)
                value = pow(left_value,right_value)
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
            
             #GOTO
            case 17:
                jump = self.quaduples[inst_pointer][3] 
                self.check_len_quad(inst_pointer)
                self.vm_handler(jump-1,offset,offset_end)
                pass

            #GOTOF
            case 18: 
                condition = self.quaduples[inst_pointer][1]
                jump = self.quaduples[inst_pointer][3]
                
                condition_real_address = self.real_address(offset, condition)
                #print  ("condition_real_address", condition_real_address)
                value = mp.get_value(condition_real_address)

                if(value):
                    inst_pointer += 1
                    self.check_len_quad(inst_pointer)
                    self.vm_handler(inst_pointer,offset,offset_end)
                    pass 
                else:
                    self.check_len_quad(inst_pointer)
                    self.vm_handler(jump-1,offset,offset_end)
                    pass 
                
            
            #EQUAL
            case 20: 
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value == right_value
                #print("EQUAL ==", value, res_real_address)
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
                
            #ASSIGN
            case 21:
                value_a = self.quaduples[inst_pointer][1]
                where = self.quaduples[inst_pointer][3] 
                
                real_add_value = self.real_address(offset,value_a)
                real_where = self.real_address(offset,where)
            
                value_v = mp.get_value(real_add_value)

                mp.set_value(real_where,value_v)
                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #GTHAN
            case 22:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value > right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #LTHAN
            case 23:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value < right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #NOTEQUAL
            case 24:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value != right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
            
            #GREATER OR EQUAL
            case 31:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value >= right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            #LESS OR EQUAL
            case 32:
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                right_real_address = self.real_address(offset, right_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                right_value = mp.get_value(right_real_address)
                
                value = left_value <= right_value
                mp.set_value(res_real_address, value)

                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass  

            #END
            case 40:
                exit()  



                

            

                