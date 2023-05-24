# # ------------------------------------------------------------
# # DATALOR: DICTIONARIES - VARIABLES TABLE
# # Mariana Favarony Avila -A01704671
# # Mario Juarez - A01411049
# #  
# # ------------------------------------------------------------
from dictionary import Dictionary
from vitual_memory import VirtualMemory
import pandas as pd

dic = Dictionary()
memory = VirtualMemory()

class DirFunc:
	def __init__(self):
		
		# Creates function directory
		self.dir_func = {
			"global": {
				"return_type": "void", 
				"scope": 0 ,
				"params": [],
				"resources": [],
	
			}
		}

		#Initializes the way in which the variables dictionary will wor, vars{}-> n mini dictioraries for each variable
		self.vars = {
			0: {
			"function_name": "global", 
			"vars": {}
		}}
		#Initialize the constant dictionary varibales
		self.constants = {}
		#RESOURCES
		# 0->int 1->float 2->bool 3-> char 4->DF
		self.resources = [0,0,0,0,0]
		#counter for function
		self.func_cont = 0 
		#memory count
		self.memory_num = 0
		
	def add_resources_temp(self,temp_i, temp_f, temp_b, temp_c):
		print("temp_ i ", temp_i)
		self.resources[0] += temp_i
		self.resources[1] += temp_f
		self.resources[2] += temp_b
		self.resources[3] += temp_c

	#_____________________________FUNCTIONS____________________#
	
	# Function for adding functions to function directory
	def add_function(self, name, scope, type, start = None):
		#SEARCHING IF THE FUNCTION ALREADY EXISTS

		if(name in self.dir_func.keys()):
			print("Function " + name + " already declared", scope)
			exit()
		else:
			# PUNTO NEURALGICO PARA RESETEAR LAS LOCALES - CAMBIAR AL PUNTO DONDE TERMINA
			# LA FUNCIÓN UNA VEZ QUE ESTE PUNTO ESTE CREADO
			memory.reset_local_temporal()


			self.dir_func[name] = {}
			self.dir_func[name]["return_type"] = type
			self.dir_func[name]["scope"] = scope
			self.dir_func[name]["params"] = []
			#Creation of a place that saves where to function quadruples start
			self.dir_func[name]["resources"] = []
			if (name != "main"):
				self.dir_func[name]["start"] = start

			#CREATING VARIABLE TABLE FOR THE FUNCTION SCOPE
			self.vars[scope] = {}
			self.vars[scope]['function_name'] = name
			self.vars[scope]['vars'] = {}

			#print(self.dir_func.keys(), self.dir_func.values())
		
	#add function resources
	def add_func_resources_glob(self):
		self.dir_func['global']['resources'].append(self.func_cont)
	
	#Get the resources from a function
	def get_resources(self, funct_name):
		if(funct_name in self.dir_func.keys()):
			return self.dir_func[funct_name]['resources']

	#Function existance?
	def search_func_exist(self, funct_name):

		if(funct_name in self.dir_func.keys()):
			return True
			
		else:
			return False
	
	def check_param(self, tipo, num_param, func):
		
		if(func in self.dir_func.keys()):
			params = self.dir_func[func]["params"]
			if(num_param > len(params)):
				print("ERROR: INVALID ARGUMENT")
				exit()
			param_type = dic.datalor_translator(params[num_param-1].upper())
			if(int(tipo) != param_type):
				#print("TIPO", type(tipo), "PARAM", type(param_type))
				print("ERROR: Type mistmatch")
				exit()
			
			
	def get_size_param(self, func_name):
		
		if(func_name in self.dir_func.keys()):
			params = self.dir_func[func_name]["params"]
			return len(params)

	#__________________VARIABLES________________________________
	
	#VARIABLES VALIDATION

	# CHECK IF THE VARIABLE ALREADY EXISTS IN THE SCOPE
	# You can declare another varibale with the same name in a specific scope different than global 
	def search_variable_declaration(self, name,scope):
		if (name in self.vars[scope]['vars'].keys()):
			return True
		else:
			return False
		
	#CHECK IF THE VARIABLE EXISTS (LOCAL/GLOBAL)
	def search_variable_existance(self, name, scope):
		if (name in self.vars[scope]['vars'].keys()):
			return self.vars[scope]['vars'][name]['type']
		else:
			if (name in self.vars[0]['vars'].keys()):
				return self.vars[0]['vars'][name]['type']
			else:
			#CHECK VAR AND SCOPE
				print('Variable not declared ', name, scope)
				exit()
		
	
	#_________________CREATING VARIABLES_________________
	#ADD VARIABLES
	def add_vars(self, name, scope, type, rowDim = None, columnDim = None):
		#Check if the variable already exists no matter the scope
		
		size = 1

		if(self.search_variable_declaration(name, scope)):
			print("Variable already declared",name)
			exit()
		else:
			# CHECK IF IT IS A NORMAL VARIABLE
			# 0 -> Normal variable
			# 1 -> Array variable
			# 2 -> Matrix variable
			type = type.upper()
			tipo = dic.datalor_translator(type)
			
				
				

			#Check if the rowDim and ColDim are 0 or 
			if(rowDim is None and columnDim is None or rowDim == 0 and columnDim == 0 ):	
				if(tipo == 6):
				#FOR VOID TYPE#IT DOESNT SAVE NOTHING IN MEMORY
					self.memory_num = 0
				else:
					self.memory_num = memory.assign_memory(tipo,scope,size)

				newVar = {name: { 'type': tipo, 'size': 0,'address': self.memory_num}}
				self.vars[scope]['vars'].update(newVar)
				print("tipo normal ", tipo)
				if (tipo != 6):
					self.resources[tipo - 1] += 1
				
				#print(self.vars.values())
			else:
				# MATRIX
				if(rowDim != 0 and columnDim != 0):
					#CALCULOS DE ROWS

					r = 1 * (rowDim) 
					r2 = r * ((columnDim-1) - (0) + 1 )
					m0 = r2
					m1 = m0/((rowDim-1)-0 + 1)
					m2 = m1/((columnDim-1)- (0) + 1 )
					
					self.memory_num = memory.assign_memory(tipo,scope,m0)

					offset = 0 + 0 * 1
					offset_end = offset + 0 * m2
					
					newVar = {name: { 'type': tipo, 'size': [[0,rowDim-1,m1,1],[0,columnDim-1,offset_end,None]],'address': self.memory_num}}
					self.vars[scope]['vars'].update(newVar)
					print("tipo matriz", tipo)
					self.resources[tipo -1] += rowDim * columnDim

					#print(self.vars.values())
				
				#ARRAY
				else:

					self.memory_num = memory.assign_memory(tipo,scope,rowDim)
					newVar = {name: { 'type': tipo, 'size': [0,rowDim-1,0,None],'address': self.memory_num}}
					self.vars[scope]['vars'].update(newVar)
					#print(self.vars.values())
					self.resources[tipo - 1] += rowDim
		

		
			
	# Checking for sizes of the arrays and matrix to be greater than 0 and not allowing the user to create for example a[0]
	def check_stype_size(self, size):
		if(size == 0):
			print('Size must be greater than 0')
			exit()

			
			#print('DEBUG' , self.vars[scope].values())
		#print(self.vars[scope]['vars'].keys())	
		#print(self.vars[scope]['vars'].values())	
		

	#ADD PARAMS
	def add_params(self, func_name, type):	
		self.dir_func[func_name]['params'].append(type)
		#print(self.dir_func.values())




	#Function for filling in the constants table with their values and address
	def add_const(self, value, type):
		#Check if the constant already exists
		if (value not in self.constants.keys()):
		#Check if the constant is an integer value
			type = type.__name__
			if(type == 'int'):
				tipo = dic.datalor_translator('CTE_INT')
				newVar = {value: {'type': tipo, 'address': memory.assign_memory(tipo,-1, 1)}}
				self.constants.update(newVar)
			else: 
				if(type == 'float'):
					tipo = dic.datalor_translator('CTE_FLOAT')
					newVar = {value: {'type': tipo, 'address': memory.assign_memory(tipo,-1,1)}}
					self.constants.update(newVar)
				# else:
				# 	if(type == 'str'):
				# 		tipo = dic.datalor_translator('CTE_CHAR')
				# 		newVar = {value: {'type': tipo, 'address': memory.assign_memory(tipo,-1)}}
				# 		self.constants.update(newVar)

			
			# print(self.constants.keys())
			# print(self.constants.values())
	#_______________Array calculus______________________#
	
	#___________________________RESOURES HANDLER____________________#
	def resources_handler(self,func_name):
		#Assgin function resources
		#print ("recursos por funcion", func_name,  self.resources)
		self.dir_func[func_name]["resources"] = self.resources
		#Reset variable resource counter
		self.resources = [0,0,0,0,0]
		

	def print(self):
		#print(tabulate(self.vars,headers='keys'))
		print("\n____________________TABLA DE FUNCIONES________________\n")
		for keys in self.dir_func.keys():	
			print('\nFuncion ', keys)
			df = pd.DataFrame.from_dict(self.dir_func[keys], orient='index')
			print(df)
		print("\n")
		
		print("____________________TABLA DE VARIABLES________________")
		for keys in self.vars.keys():	
			print('\nScope ', self.vars[keys]['function_name'])
			df = pd.DataFrame.from_dict(self.vars[keys]['vars'], orient='index')
			print(df)
		print("\n")

		print("____________________TABLA DE CONSTANTES_______________")
		
		df = pd.DataFrame.from_dict(self.constants, orient='index')
		print(df)
		
		print("\n")
		print("RESOURCES", self.resources)

	#GET ADDRESS FOR CREATING QUADRUPLE
	#def get_address(self, item, scope):

	



