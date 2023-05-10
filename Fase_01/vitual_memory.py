# -----------------------------------------------------------
# DATALOR: ASSIGNING VIRTUAL MEMORY
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# Range for every category
# -----------------------------------------------------------

class VirtualMemory:
    
    def __init__(self):
    # INICIO + TAMAÑO  = FIN
        #_________SIZE_________
        
            #GLOBALES
        self.g_i_size = 1999
        self.g_f_size = 1999
        self.g_c_size = 1999
        self.g_df_size = 1999

         #LOCALES
        self.l_i_size = 1999
        self.l_f_size = 1999
        self.l_c_size = 1999
        self.l_df_size = 1999

            #TEMPORALES
        self.t_i_size = 1999
        self.t_f_size = 1999
        self.t_c_size = 1999
        self.t_b_size = 1999

            #CONSTANTES
        self.c_i_size = 1999
        self.c_f_size = 1999
        self.c_c_size = 1999

        #________START______

        #GLOBALES
        self.g_i_init = 1000
        self.g_f_init = 3000
        self.g_c_init = 5000
        self.g_df_init = 7000

        #LOCALES
        self.l_i_init = 9000
        self.l_f_init = 12000
        self.l_c_init = 15000
        self.l_df_init = 18000

        #TEMPORALES
        self.t_i_init = 15000
        self.t_f_init = 17000
        self.t_c_init = 19000
        self.t_b_init = 21000

        #CONSTANTES
        self.c_i_init = 23000
        self.c_f_init = 25000
        self.c_c_init = 27000

        #_______COUNTERS_______

        #GLOBALES
        self.g_i_cont = 0
        self.g_f_cont = 0
        self.g_c_cont = 0
        self.g_df_cont = 0

        #LOCALES
        self.l_i_cont = 0
        self.l_f_cont = 0
        self.l_c_cont = 0
        self.l_df_cont = 0

        #TEMPORALES
        self.t_i_cont = 0
        self.t_f_cont = 0
        self.t_c_cont = 0
        self.t_b_cont = 0

        #CONSTANTES
        self.c_i_cont = 0
        self.c_f_cont = 0
        self.c_c_cont = 0

    #CHECK IF THE STACK IS FULL
    def overflow(self, cont, size):
        #GETTING RANGE
        if(cont > size):
            print('overflow')
            exit()
            
    #RESET DE LAS VARIABLES LOCALES/TEMPORALES
    def reset_local_temporal(self):
        self.l_i_cont = 0
        self.l_f_cont = 0
        self.l_c_cont = 0
        self.l_df_cont = 0


    # ASSIGN ADDRESS MEMORY TO THE VARIABLES
    def assign_memory(self, tipo, scope):
    #GLOBAL 
        # 1 int # 2 float # 3 char 
        address = 0 
        if(scope == 0 ):
            match tipo:  
                case 1:
                    #Overflow checker
                    self.overflow(self.g_i_cont, self.g_i_size)
                    address = self.g_i_init + self.g_i_cont
                    self.g_i_cont += 1
                    #print(address)
                    return address
                case 2:
                    #Overflow checker
                    self.overflow(self.g_f_cont, self.g_f_size)
                    address = self.g_f_init + self.g_f_cont
                    self.g_f_cont += 1
                    #print(address)
                    return address

                case 3: 
                    #Overflow checker
                    self.overflow(self.g_c_cont, self.g_c_size)
                    #returns the address 
                    address =  self.g_c_init + self.g_c_cont
                    self.g_c_cont += 1
                    #print(address)
                    return address
                case 6:
                    #Overflow checker
                    self.overflow(self.g_df_cont, self.g_df_size)
                    #returns the address
                    address = self.g_df_init + self.g_df_cont
                    self.g_df_cont += 1
                    #print(address)
                    return address
                
        #CONSTANTS       
        else:
            #SCOPE -1 = cte 
            if (scope == -1):
                match tipo:
                    #INT
                    case 28:
                        #Overflow checker
                        self.overflow(self.c_i_cont, self.c_i_size)
                        #returns the address
                        address = self.c_i_init + self.c_i_cont
                        self.c_i_cont += 1
                        #print(address)
                        return address
                    #FLOAT
                    case 29:
                        self.overflow(self.c_f_cont, self.c_f_size)
                        #return the address
                        address = self.c_f_init + self.c_f_cont
                        self.c_f_cont += 1
                        #print(address)
                        return address
                    #CHAR
                    case 30:
                        self.overflow(self.c_c_cont, self.c_c_size)
                        #return the address
                        address = self.c_c_init + self.c_c_cont
                        self.c_c_cont += 1
                        #print (address)
                        return address
            #LOCAL
            else:
                match tipo:
                    #INT
                    case 1:
                        #Overflow checker
                        self.overflow(self.l_i_cont, self.l_i_size)
                        #returns the address
                        address = self.l_i_init + self.l_i_cont
                        self.l_i_cont += 1
                        #print(address)
                        return address
                    #FLOAT
                    case 2:
                        self.overflow(self.l_f_cont, self.l_f_size)
                        #return the address
                        address = self.l_f_init + self.l_f_cont
                        self.l_f_cont += 1
                        #print(address)
                        return address
                    #CHAR
                    case 3:
                        self.overflow(self.l_c_cont, self.l_c_size)
                        #return the address
                        address = self.l_c_init + self.l_c_cont
                        self.l_c_cont += 1
                        #print (address)
                        return address
                    #DATAFRAME
                    case 6:
                        self.overflow(self.l_df_cont, self.l_df_size)
                        #return the address
                        address = self.l_df_init + self.l_df_cont
                        self.l_df_cont += 1