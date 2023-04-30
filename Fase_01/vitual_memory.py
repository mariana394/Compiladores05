# -----------------------------------------------------------
# DATALOR: ASSIGNING VIRTUAL MEMORY
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# Range for every category
# -----------------------------------------------------------

class VirtualMemory:
    
    def __init__(self):
    # INICIO + TAMAÑO  = FIN
        #SIZE
        self.g_i_size = 1999
        self.g_f_size = 1999
        self.g_c_size = 1999

        self.l_i_size = 1999
        self.l_f_size = 1999
        self.l_c_size = 1999

        self.t_i_size = 1999
        self.t_f_size = 1999
        self.t_c_size = 1999

        self.c_i_size = 1999
        self.c_f_size = 1999
        self.c_c_size = 1999

        #START
        self.g_i_init = 1000
        self.g_f_init = 3000
        self.g_c_init = 5000

        self.l_i_init = 7000
        self.l_f_init = 9000
        self.l_c_init = 11000

        self.t_i_init = 13000
        self.t_f_init = 15000
        self.t_c_init = 17000

        self.c_i_init = 19000
        self.c_f_init = 21000
        self.c_c_init = 23000

        #COUNTERS
        self.g_i_cont = 0
        self.g_f_cont = 0
        self.g_c_cont = 0

        self.l_i_cont = 0
        self.l_f_cont = 0
        self.l_c_cont = 0

        self.t_i_cont = 0
        self.t_f_cont = 0
        self.t_c_cont = 0

        self.c_i_cont = 0
        self.c_f_cont = 0
        self.c_c_cont = 0

    #CHECK IF THE STACK IS FULL
    def overflow(self, cont, size):
        #GETTING RANGE
        if(cont > size):
            print('overflow')
            exit()
            

    # ASSIGN ADDRESS MEMORY TO THE VARIABLES
    def assign_memory(self, tipo, scope):
    #GLOBAL 
        # 1 int # 2 float # 3 char 
        address = '' 
        if(scope == 0 ):
            match tipo:  
                case 1:
                    #Overflow checker
                    self.overflow(self.cont_int_global, self.size_int_global)
                    address = self.g_i_init + self.g_i_cont
                    self.g_i_cont += 1
                    return address
                case 2:
                    #Overflow checker
                    self.overflow(self.cont_float_global, self.size_float_global)
                    address = self.g_f_init + self.g_f_cont
                    self.g_f_cont += 1
                    return address

                case 3: 
                    #Overflow checker
                    self.overflow(self.cont_char_global, self.size_char_global)
                    #returns the address 
                    address =  self.g_c_init + self.g_c_cont
                    self.g_c_cont += 1
                    return address
         
            
    #LOCAL
        else:
            print('tacos')