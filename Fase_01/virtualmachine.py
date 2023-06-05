# -----------------------------------------------------------
# DATALOR: Virtual Machine
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# Virtual Machine....
# -----------------------------------------------------------
from memory_map import MemoryMap
#PYTHON
import pandas as pd

import sys


sys.setrecursionlimit(5000)
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
        self.temporal_offset= []
        self.size_memory = []
        # 0 -> int, 1 -> Float, 2 -> Char , 3 -> DF
        self.t_param_counter = [0,0,0,0]
        self.dir_base = False
        self.model = None
       
       
    
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
        # print("________VIRTUAL MACHINE__________")
        #print("QUAD:\n ", self.quaduples)
        # print("\n RES: ",self.resources)
        # print("\n CONST: ",self.const)
        # print("RECURSOS MAIN",mp.res_global(self.resources[0]))
        main_offset = mp.res_global(self.resources[0])
        print("MAIN OFFSET", main_offset)
        end_main = mp.res_global(self.resources[1])
        print("END MAIN", end_main)
        self.sort_const()
        
        self.vm_handler(0, main_offset, end_main)

        
        
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
            address = (virtual_address - self.l_c_init + offset[2])
            return [2,address]
        
        #DATAFRAME
        if(virtual_address >= self.l_df_init and virtual_address < self.t_i_init):
            address = (virtual_address - self.l_df_init + offset[4])
            return [4,address]
        
         #________TEMPORALES________
       #INT
        if(virtual_address >= self.t_i_init and virtual_address < self.t_f_init):
            address = (virtual_address - self.t_i_init + offset[5])
            return [5,address]
       
       #FLOAT
        if(virtual_address >= self.t_f_init and virtual_address < self.t_c_init):
            address = (virtual_address - self.t_f_init + offset[6])
            return [6,address]
        
        #CHAR
        if(virtual_address >= self.t_c_init and virtual_address < self.t_b_init):
            address = (virtual_address - self.t_c_init + offset[7])
            return [7,address]
        
        #BOOL
        if(virtual_address >= self.t_b_init and virtual_address < self.c_i_init):
            address = (virtual_address - self.t_b_init + offset[8])
            return [8,address]
        
        
        #DATAFRAME
        if(virtual_address >= self.t_df_init and virtual_address < self.t_tp_init):
            address = (virtual_address - self.t_df_init + offset[9])
            return [9,address]

        #________CONSTANTES________
        #INT
        if(virtual_address >= self.c_i_init and virtual_address < self.c_f_init):
            address = (virtual_address - self.c_i_init)
            #5 -> int Const
            return [11, address]
        
        #FLOAT
        if(virtual_address >= self.c_f_init and virtual_address < self.c_c_init):
            address = (virtual_address - self.c_f_init)
            #6 -> float Const
            return [12, address]
        
        #CHAR
        if(virtual_address >= self.c_c_init and virtual_address < self.t_df_init):
            address = (virtual_address - self.c_c_init)
            #7 -> char Const
            return [13, address]
        
        #__________POINTERS__________
        if(virtual_address >= self.t_tp_init and virtual_address < self.t_tp_init + 1999):
            
            address = (virtual_address - self.t_tp_init)
            new_address = mp.get_value([10,address])
            
            if (self.dir_base):
                return [10, address]
            else : 
                return  self.real_address(offset,new_address)
            

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
            #self.print_todo()
            exit()

    def vm_handler(self, inst_pointer, offset, offset_end):
        operation = self.quaduples[inst_pointer][0]
       # print("Curr_quad ", self.quaduples[inst_pointer] )
        match operation:

            #PRINT
            case 7:
                value_p = self.quaduples[inst_pointer][3]
                real_print_address =  self.real_address(offset, value_p)   
               # print("PRINT ADD",real_print_address)
                print_v = mp.get_value(real_print_address)
                
                print(print_v)
                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
            
            #READ ->INCOMPLETO
            case 8: 
                value = self.quaduples[inst_pointer][1]
                read_address = self.quaduples[inst_pointer][3]

                real_add_value = self.real_address(offset, value)
                real_read_add = self.real_address(offset, read_address)

                real_value = mp.get_value(real_add_value)
                real_value = real_value.replace('"','')
                real_value = real_value.replace("'",'')
               # print('real value', real_value)
                mp.set_value(real_read_add,pd.read_csv(real_value))
                #print(pd.read_csv(real_value))
                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

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
                #self.print_todo()

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
                
            #GOTOV
            case 19:
                condition = self.quaduples[inst_pointer][1]
                jump = self.quaduples[inst_pointer][3]

                condition_real_address = self.real_address(offset, condition)
                #print  ("condition_real_address", condition_real_address)
                value = mp.get_value(condition_real_address)
                #print(value, "IP:",inst_pointer,"jump", jump)
                if(value):
                    self.check_len_quad(inst_pointer)
                    self.vm_handler(jump-1,offset,offset_end)
                    pass 
                else:
                    inst_pointer += 1
                    self.check_len_quad(inst_pointer)
                    self.vm_handler(inst_pointer,offset,offset_end)
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
                
                if(where >= 33000):
                    print('estoy por poner un valor de pointer')

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

            #RETURN
            case 33:
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

            #END FUNCTION
            case 34:
                size = self.size_memory.pop()
                #print("RELEASE MEMORY",size)
                #print("END FUNCTION BEFORE RELEASE MEMORY 1")
                #self.print_todo()
                mp.release_memory(size)
                #print("END FUNCTION AFTER RELEASE MEMORY 1")
                #self.print_todo()
                #Llama a la variable que guarda los size de memoria
                #Usa esos size para liberar ese espacio de memoria
                #Termina la llamada recursiva aquí
            #ERA
            case 35:
                g_int = self.quaduples[inst_pointer][2]
                t_int = self.quaduples[inst_pointer][3]
                g_float = self.quaduples[inst_pointer+1][2]
                t_float = self.quaduples[inst_pointer+1][3]
                g_bool = self.quaduples[inst_pointer+3][2]
                t_bool = self.quaduples[inst_pointer+3][3]
                g_char = self.quaduples[inst_pointer+2][2]
                t_char = self.quaduples[inst_pointer+2][3]
                g_df = self.quaduples[inst_pointer+4][2]
                t_df = self.quaduples[inst_pointer+4][3]
                t_pointer = self.quaduples[inst_pointer+5][3]

                memory_size = [g_int, g_float, g_char, g_bool, g_df, t_int, t_float, t_char, t_bool, t_df, t_pointer]
                #print('MEMORIA RECURSIVA', memory_size)
                end_era = mp.res_global(memory_size)
                #Guardamos el tamaño para liberar memoria en endfunc 
                self.size_memory.append(memory_size)
                #Guardamos el offset para usarlo en gosub
                self.temporal_offset = end_era
                inst_pointer += 6
                self.vm_handler(inst_pointer,offset,offset_end)
                pass
                #Llama al tamaño y crea el espacio en memoria
                #Salto de +6 en cuadruplos
                #Transformar las duplas de los ERA en una lista para
                #asignar memoria

            #GOSUB
            case 36:
                jump = self.quaduples[inst_pointer][3]
                self.t_param_counter= [0,0,0,0]
                self.vm_handler(jump - 1,offset_end, self.temporal_offset)
                inst_pointer += 1
                self.vm_handler(inst_pointer, offset, offset_end)
                pass

            #PARAMETER
            case 37:
                left_addr = self.quaduples[inst_pointer][1]
                left_real_address = self.real_address(offset, left_addr)
                param_address = 0
                #print("left_real_address", left_real_address)
                if (left_real_address[0] == 0 or left_real_address[0] == 5 or left_real_address[0] == 11):
                    param_address = self.l_i_init + self.t_param_counter[0] 
                    self.t_param_counter[0] += 1
                if (left_real_address[0] == 1 or left_real_address[0] == 6 or left_real_address[0] == 12):
                    param_address = self.l_f_init + self.t_param_counter[1]
                    self.t_param_counter[1] += 1
                if (left_real_address[0] == 2 or left_real_address[0] == 7 or left_real_address[0] == 13):
                    param_address = self.l_c_init + self.t_param_counter[2]
                    self.t_param_counter[2] += 1
                if (left_real_address[0] == 4 or left_real_address[0] == 9):
                    param_address = self.l_df_init + self.t_param_counter[3]
                    self.t_param_counter[3] += 1
                #print("param_address", param_address)
                param_real_address = self.real_address(offset_end, param_address)

                left_value = mp.get_value(left_real_address)
                mp.set_value(param_real_address,left_value)
                #self.print_todo()
                self.vm_handler(inst_pointer+1,offset,offset_end)
                pass

                
            # #GOSPECIAL
            # case 38:

            #VER-> VERIFICATION RANGE OF ARR-MAT
            case 39:
                value = self.quaduples[inst_pointer][1]
                linferior = self.quaduples[inst_pointer][2]
                lsuperior = self.quaduples[inst_pointer][3]

                value_real_address = self.real_address(offset, value)

                value = mp.get_value(value_real_address)

                if value >= linferior and value <= lsuperior:
                    
                    inst_pointer += 1
                    self.check_len_quad(inst_pointer)
                    self.vm_handler(inst_pointer,offset,offset_end)
                    pass
                
                else:
                    print("ERROR: INDEX OUT OF RANGE")
                    exit()

            #PLUS_DIR_BASE
            case 40:
                self.dir_base = True
                left_addr = self.quaduples[inst_pointer][1]
                right_addr = self.quaduples[inst_pointer][2]
                res = self.quaduples[inst_pointer][3] 
                
                left_real_address = self.real_address(offset, left_addr)
                res_real_address = self.real_address(offset, res)

                left_value = mp.get_value(left_real_address)
                print("el valor de la dirección izquierda es 2:", left_value)
                value = left_value + right_addr
                print('LUGAR DEL POINTER ES: ', res)
                print('EL LUGAR QUE OCUPARE CON', value, 'ES DEL POINTER', res_real_address)
                mp.set_value(res_real_address, value)
                #self.print_todo()
                self.dir_base = False
                inst_pointer += 1
                self.check_len_quad(inst_pointer)
                self.vm_handler(inst_pointer,offset,offset_end)
                pass

            case 'special':
                import matplotlib.pyplot as plt 
                from datetime import date
                from sklearn.model_selection import train_test_split
                from sklearn.linear_model import LinearRegression
                import statsmodels.api as sm
                import seaborn as sns

                from statsmodels.tsa.stattools import adfuller
                from pmdarima import auto_arima
                from pandas.plotting import autocorrelation_plot

                from sklearn.metrics import mean_squared_error
                from math import sqrt

                import matplotlib.pyplot as plt
                from matplotlib import pyplot
                from scipy.stats import skew, kurtosis


                special_function = self.quaduples[inst_pointer][3]
                print("SPECIAL FUNCTION", special_function)

                match special_function:
                    case 'exploration':
                        i = 1
                        go_special = self.quaduples[inst_pointer + i][0]
                        #DATAFRAME
                        param1 = None
                        #CONSTANTE
                        param2 = None
                        while go_special != 38:
                            print('CUADRUPLO ACTUAL', self.quaduples[inst_pointer + i])
                            go_special = self.quaduples[inst_pointer + i][0]
                            param = self.quaduples[inst_pointer + i][3]
                            param_value = self.quaduples[inst_pointer + i][1]
                                 #Quiere decir que es el parametro 1
                            if (param == 1):
                                param1 = param_value
                            if (param == 2):
                                param2 = param_value
                            i += 1
                                #Quiere decir que es el parametro 2
                        print ('PARAMETRO 1', param1, 'PARAMETRO 2', param2)
                        param1_real_address = self.real_address(offset, param1)
                        param2_real_address = self.real_address(offset, param2)
                        print('REAL ADDRESS PARAM', param1_real_address)
                        print('VALOR DE LOS PARAMETROS',mp.get_value(param1_real_address))
                        print('VALOR DE LOS PARAMETROS',mp.get_value(param2_real_address))
                        param1 = mp.get_value(param1_real_address)
                        param2 = mp.get_value(param2_real_address)
                        #IF param2 == ? ponte a hacer algo
                        
                         #TEMPORAL DATAFRAME
                        save = self.quaduples[inst_pointer + i - 1][3]
                        save_real_address = self.real_address(offset, save)
                        print('SAVE REAL ADDRESS', save_real_address, 100)
                    
                       
                        print("ENTRO AL MATCH param2")

                        match param2:
                            #Estadisticos de posicion
                            case 1:
                                estad_posi = param1.describe()
                                #estad_posi = [param1.mean(numeric_only=True),param1.median(numeric_only=True),param1.mode(numeric_only=True)]
                                mp.set_value(save_real_address, estad_posi)
                                print("\n_____ESTADÍSTICOS DESCRIPTIVOS________\n")
                                print(estad_posi)
                                inst_pointer += i
                                self.check_len_quad(inst_pointer)
                                self.vm_handler(inst_pointer,offset,offset_end)
                                pass

                            case 2:
                                estad_disp = [param1.mode(numeric_only = True),param1.median(numeric_only = True),param1.var(numeric_only = True)]
                                print("______________ESTADÍSTICOS DE DISPERSIÓN__________")
                                print("\nMODA:\n",estad_disp[0] )
                                print("\nMEDIANA:\n",estad_disp[1])
                                print("\nVARIANZA:\n ",estad_disp[2])
                                inst_pointer += i
                                self.check_len_quad(inst_pointer)
                                self.vm_handler(inst_pointer,offset,offset_end)
                                pass

                            case 3:   
                                print("______________ASIMETRIA-KURTOSIS__________")                           
                                numeric_columns = param1.select_dtypes(include=['int', 'float']).columns
                                for column in numeric_columns:
                                    skewness = skew(param1[column])
                                    kurt = kurtosis(param1[column])
                                    print("Asimetría de", column, ":", skewness)
                                    print("Curtosis de", column, ":", kurt)
                                
                                inst_pointer += i
                                self.check_len_quad(inst_pointer)
                                self.vm_handler(inst_pointer,offset,offset_end)
                                pass

                                
                    case 'financial_state':
                        i = 1
                        go_special = self.quaduples[inst_pointer + i][0]
                        #DATAFRAME
                        costos = None
                        ventas= None
                        #fechas
                        initial = None
                        final = None
                        while go_special != 38:
                            print('CUADRUPLO ACTUAL', self.quaduples[inst_pointer + i])
                            go_special = self.quaduples[inst_pointer + i][0]
                            param = self.quaduples[inst_pointer + i][3]
                            param_value = self.quaduples[inst_pointer + i][1]
                                 #Quiere decir que es el parametro 1
                            if (param == 1):
                                costos = param_value
                            if (param == 2):
                                ventas = param_value
                            if(param == 3):
                                initial= param_value
                            if(param == 4):
                                final= param_value

                            i += 1
                    
                        costos_real_address = self.real_address(offset, costos)
                        ventas_real_address = self.real_address(offset, ventas)
                        initial_real_address = self.real_address(offset, initial)
                        final_real_address = self.real_address(offset, final)
                        # print('REAL ADDRESS PARAM', param1_real_address)
                        # print('VALOR DE LOS PARAMETROS',mp.get_value(param1_real_address))
                        # print('VALOR DE LOS PARAMETROS',mp.get_value(param2_real_address))
                        costos = mp.get_value(costos_real_address)
                        ventas = mp.get_value(ventas_real_address)
                        initial = mp.get_value(initial_real_address)
                        final = mp.get_value(final_real_address)
                        
                        
                         #TEMPORAL DATAFRAME
                        save = self.quaduples[inst_pointer + i - 1][3]
                        save_real_address = self.real_address(offset, save)
                        print('SAVE REAL ADDRESS', save_real_address, 100)
                    
                        initial = pd.Timestamp(initial)
                        final = pd.Timestamp(final)
                        print("ENTRO AL MATCH param2")
                        
                        costos['Fecha'] = costos['Fecha'].apply(pd.Timestamp)
                        ventas['Fecha'] = ventas['Fecha'].apply(pd.Timestamp)

                        costos_filtrado = costos[(costos['Fecha']>= initial) & (costos['Fecha'] <= final)]
                        ventas_filtrado = ventas[(ventas['Fecha'] >= initial) & (ventas['Fecha'] <= final)]

                        # Calcular el total de costos por categoría
                        costos_filtrado = costos.groupby('Categoría')['Costo'].sum()

                        # Calcular el total de ventas por producto
                        ventas_filtrado = ventas.groupby('Producto')['Total'].sum()

                        # Calcular el total de ventas
                        total_ventas = ventas_filtrado.sum()

                        # Calcular el margen de contribución
                        margen_contribucion = total_ventas - costos_filtrado.sum()

                        # Calcular el porcentaje de margen de contribución
                        porcentaje_margen = (margen_contribucion / total_ventas) * 100

                        # Imprimir el estado financiero
                        print('Estado Financiero')
                        print('-----------------')
                        print('Total Ventas:', total_ventas)
                        print('Costos por Categoría:')
                        print(costos_filtrado)
                        print('Margen de Contribución:', margen_contribucion)
                        print('Porcentaje de Margen de Contribución:', porcentaje_margen, '%')        
                            

                        print(self.quaduples[inst_pointer + i - 1])
                        inst_pointer += i
                        self.check_len_quad(inst_pointer)
                        self.vm_handler(inst_pointer,offset,offset_end)
                        pass
                       
                    case 'season_analysis':
                        i = 1
                        go_special = self.quaduples[inst_pointer + i][0]
                        #DATAFRAME
                        param1 = None
                        
                        while go_special != 38:
                            print('CUADRUPLO ACTUAL', self.quaduples[inst_pointer + i])
                            go_special = self.quaduples[inst_pointer + i][0]
                            param = self.quaduples[inst_pointer + i][3]
                            param_value = self.quaduples[inst_pointer + i][1]
                                 #Quiere decir que es el parametro 1
                            if (param == 1):
                                ventas = param_value
                            i += 1
                                #Quiere decir que es el parametro 2
                        ventas_real_address = self.real_address(offset, ventas)
                        ventas = mp.get_value(ventas_real_address)
                      
                        #TEMPORAL DATAFRAME
                        save = self.quaduples[inst_pointer + i - 1][3]
                        save_real_address = self.real_address(offset, save)
                        
                        ventas['Fecha'] = ventas['Fecha'].apply(pd.Timestamp)

                        # Agregar una columna "Mes" que contenga solo el mes de la fecha
                        ventas['Mes'] = ventas['Fecha'].dt.month

                        # Agrupar por mes y producto 
                        ventas_por_mes = ventas.groupby(['Mes', 'Producto'])['Total'].sum().reset_index()

                        # El producto estrella
                        productos_mas_vendidos_por_mes = ventas_por_mes.loc[ventas_por_mes.groupby('Mes')['Total'].idxmax()]

                        print('PRODUCTOS MAS VENDIDOS POR MES:')
                        print('-----------------')
                        print(productos_mas_vendidos_por_mes)
                        ventas = ventas.drop('Mes', axis=1)
                        inst_pointer += i
                        self.check_len_quad(inst_pointer)
                        self.vm_handler(inst_pointer,offset,offset_end)
                        pass

                    case 'trend_prediction':
                        i = 1
                        go_special = self.quaduples[inst_pointer + i][0]
                        #DATAFRAME
                        param1 = None
                        
                        while go_special != 38:
                            print('CUADRUPLO ACTUAL', self.quaduples[inst_pointer + i])
                            go_special = self.quaduples[inst_pointer + i][0]
                            param = self.quaduples[inst_pointer + i][3]
                            param_value = self.quaduples[inst_pointer + i][1]
                                 #Quiere decir que es el parametro 1
                            if (param == 1):
                                data_arima = param_value
                            i += 1
                                #Quiere decir que es el parametro 2
                        data_arima_real_address = self.real_address(offset, data_arima)
                        data_arima = mp.get_value(data_arima_real_address)
                        print('arima domingo', data_arima)
                        #TEMPORAL DATAFRAME
                        save = self.quaduples[inst_pointer + i - 1][3]
                        save_real_address = self.real_address(offset, save)
                        arima = data_arima
                        data_arima = data_arima.set_index(['Month'])
                        #CALCULAR LOS VALORES DE P,D,Q QUE SE ADECUAN A LOS DATOS
                        stepwise_fit = auto_arima(data_arima['Sales'], trace=True,suppress_warnings=True)
                        p = stepwise_fit.order[0]
                        d = stepwise_fit.order[1]
                        q = stepwise_fit.order[2]

                        #DATOS PARA EL MODELO
                        X = data_arima.values
                        size = int(len(X) * 0.66)
                        train, test = X[0:size], X[size:len(X)]
                        history = [x for x in train]
                        predictions = list()

                        #EJECUTAR LA PREDICCION
                        for t in range(len(test)):
                            model = sm.tsa.ARIMA(history, order=(p,q,d))
                            model_fit = model.fit()
                            output = model_fit.forecast()
                            yhat = output[0]
                            predictions.append(yhat)
                            obs = test[t]
                            history.append(obs)
                            #print('predicted=%f, expected=%f' % (yhat, obs))
                        
                        #MEDICIONES
                        rmse = sqrt(mean_squared_error(test, predictions))
                        print('Test RMSE: %.3f' % rmse)
                        #GRAFICAR RESULTADO
                        print('PREDICCION-ARIMA:')
                        pyplot.plot(test, label='historico')
                        pyplot.plot(predictions, color='red', label ='prediccion')
                        plt.xlabel('Mes')
                        plt.ylabel('Ventas')
                        plt.legend()
                        plt.title('Pronostico de Ventas')
                        today = date.today().strftime("%Y-%m-%d")
                        df = pd.DataFrame(test, columns=['Historico'])
                        df['Prediccion'] = predictions
                        file_name = f'pronostico_ventas_{today}.xlsx'
                        df.to_excel(file_name, index=False)

                        print('PREDICCION:')
                        print('-----------------')
                        print('El archivo ha sido creado con exito!')
                        image_name = f'pronostico_de_ventas_{today}.png'
                        #pyplot.show()

                        plt.savefig(image_name, dpi=300)  # Ruta y nombre del archivo de imagen

                       
                        inst_pointer += i
                        self.check_len_quad(inst_pointer)
                        self.vm_handler(inst_pointer,offset,offset_end)
                        pass


                    case 'dummi_regression':
                        i = 1
                        go_special = self.quaduples[inst_pointer + i][0]
                        #DATAFRAME
                        ventas_rl= None
                        #META
                        meta = None
                        while go_special != 38:
                            go_special = self.quaduples[inst_pointer + i][0]
                            param = self.quaduples[inst_pointer + i][3]
                            param_value = self.quaduples[inst_pointer + i][1]
                                 #Quiere decir que es el parametro 1
                            if (param == 1):
                                ventas_rl = param_value
                                
                            if (param == 2):
                                meta = param_value

                            i += 1
                    
                        ventas_real_address = self.real_address(offset, ventas_rl)
                        meta_real_address = self.real_address(offset, meta)
                        # print('REAL ADDRESS PARAM', param1_real_address)
                        # print('VALOR DE LOS PARAMETROS',mp.get_value(param1_real_address))
                        # print('VALOR DE LOS PARAMETROS',mp.get_value(param2_real_address))
                        ventas_rl = mp.get_value(ventas_real_address)
                        ventas_rl = ventas_rl.drop('Mes', axis=1)

                        print("domingo", ventas_rl)
                        meta = mp.get_value(meta_real_address)
                        
                        #Matriz de correlacion
                        print('MATRIZ DE CORRELACION')
                        print('-----------------')
                        matriz_corr = ventas_rl.corr(numeric_only=True)
                        print(matriz_corr)

                        #filtrar por el umbral
                        #limpiar el data set
                        # ventas_rl = ventas_rl.dropna()
                        
                        #ENTRENAMIENRO
                        X = ventas_rl[['Cantidad', 'Precio unitario']]

                        
                        meta = meta.replace("'", "")
                        y = ventas_rl[meta]
                        #20% para test 80% para train

                        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
                        #correr el modelo
                        print("entrenamiento",X_train)
                        self.model = LinearRegression()
                        self.model.fit(X_train, y_train)

                        # #Predecir
                        # y_pred = self.model.predict(X_test)

                        # #metricas
                        # # metrica = self.model.score(X_test, y_test)
                       
                        # print('Modelo entrenado con ',  metrica, ' de confianza')
                        inst_pointer += i
                        self.check_len_quad(inst_pointer)
                        self.vm_handler(inst_pointer,offset,offset_end)
                        pass
                    
                    case 'model_predict':
                        i = 1
                        go_special = self.quaduples[inst_pointer + i][0]
                        #DATAFRAME
                        param1 = None
                        
                        while go_special != 38:
                            print('CUADRUPLO ACTUAL', self.quaduples[inst_pointer + i])
                            go_special = self.quaduples[inst_pointer + i][0]
                            param = self.quaduples[inst_pointer + i][3]
                            param_value = self.quaduples[inst_pointer + i][1]
                                 #Quiere decir que es el parametro 1
                            if (param == 1):
                                predecir = param_value
                            i += 1
                                #Quiere decir que es el parametro 2
                        predecir_real_address = self.real_address(offset, predecir)
                        predecir = mp.get_value(predecir_real_address)
                        #asegurarnos de que todos los datos son numericos
                        # predecir = predecir.dropna()
                        
                        print("domingo pred", predecir.select_dtypes(include=['float', 'int']))


                        y_pred = self.model.predict(predecir.select_dtypes(include=['float', 'int']))
                        predecir['Prediccion_Total'] = y_pred
                        print("domingo pred", y_pred)
                        today = date.today().strftime("%Y-%m-%d")

                        file_name = f'prediccion_{today}.xlsx'

                        predecir.to_excel(file_name, index=False)

                        print('PREDICCION:')
                        print('-----------------')
                        print('El archivo ha sido creado con exito!')

                        inst_pointer += i
                        self.check_len_quad(inst_pointer)
                        self.vm_handler(inst_pointer,offset,offset_end)
                        pass


            #END
            case 41:
                self.print_todo()

                exit()  



                

            

                