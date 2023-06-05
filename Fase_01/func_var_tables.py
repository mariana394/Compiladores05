# # ------------------------------------------------------------
# # DATALOR: DICTIONARIES - VARIABLES TABLE
# # Mariana Favarony Avila -A01704671
# # Mario Juarez - A01411049
# #  
# # ------------------------------------------------------------
from dictionary import Dictionary
from vitual_memory import VirtualMemory
import pandas as pd
import json

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
		# 0->int 1->float 2->Char 3-> Bool 4->DF
		self.resources = [0,0,0,0,0]
		#counter for function
		self.func_cont = 0 
		#memory count
		self.memory_num = 0
		
	#Function that add temporal variables to the function directory
	#It receives a list of the temporal variables and the name of the function
	#then it adds the temporal variables to the function directory
	def add_resources_temp(self,temp_i, temp_f, temp_b, temp_c, temp_df,temp_pt,func_name):
		#print("temp_ i ", temp_i)
		#if(func_name != 'global'): 
		self.dir_func[func_name]["resources"].append(temp_i) 
		self.dir_func[func_name]["resources"].append(temp_f) 
		self.dir_func[func_name]["resources"].append(temp_c)
		self.dir_func[func_name]["resources"].append(temp_b) 
		self.dir_func[func_name]["resources"].append(temp_df) 
		self.dir_func[func_name]["resources"].append(temp_pt) 

		

	#_____________________________FUNCTIONS____________________#
	
	# It adds a function to the function directory
	# It receives the name of the function, the scope, the type of the function 
	# and the start of the function if its necesary
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
			self.dir_func[name]["return_type"] = dic.datalor_translator(type.upper())
			self.dir_func[name]["scope"] = scope
			self.dir_func[name]["params"] = []
			#Creation of a place that saves where to function quadruples start
			self.dir_func[name]["resources"] = []

			match type:
				case "int":
					self.dir_func["global"]["resources"][0] += 1
				case "float":
					self.dir_func["global"]["resources"][1] += 1
				case "char":
					self.dir_func["global"]["resources"][2] += 1
					
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
	#It receives the name of the function and 
	# returns the resources of the function
	def get_resources(self, funct_name):
		if(funct_name in self.dir_func.keys()):
			return self.dir_func[funct_name]['resources']

	#Function existance validation
	#It receives the name of the function and
	# returns true if the function exists and false if it doesn't
	def search_func_exist(self, funct_name):

		if(funct_name in self.dir_func.keys()):
			return True
			
		else:
			return False
	
	#Function type validation
	#It receives the name of the funtion, the number of the parameter and the type of the parameter
	#it will just print an error if the type of the parameter doesn't match the type of the function parameter
	def check_param(self, tipo, num_param, func):
		
		if(func in self.dir_func.keys()):
			params = self.dir_func[func]["params"]
			if(num_param > len(params)):
				print("ERROR: INVALID ARGUMENT")
				exit()
			param_type =  params[num_param-1]
			if(int(tipo) != param_type):
				#print("TIPO", type(tipo), "PARAM", type(param_type))
				print("ERROR: Type mistmatch")
				exit()
			
	#Function that return the size of the parameters of a function
	#It receives the name of the function and returns the size of the parameters
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
	#It receives the name of the variable and the scope
	#It returns the type and the address of the variable
	def search_variable_existance(self, name, scope):
		if (name in self.vars[scope]['vars'].keys()):
			
			return [(self.vars[scope]['vars'][name]['type']),(self.vars[scope]['vars'][name]['address'])] 
		else:
			
			if (name in self.vars[0]['vars'].keys()):
				return [self.vars[0]['vars'][name]['type'], self.vars[0]['vars'][name]['address']]
			else:
			#CHECK VAR AND SCOPE
				print('Variable not declared ', name, scope)
				exit()
		
	#_________________CREATING VARIABLES_________________
	#ADD VARIABLES
	#It receives the name of the variable, the scope, the type of the variable and the dimensions of the variable
	#It will just print an error if the variable already exists
	def add_vars(self, name, scope, types, rowDim = None, columnDim = None):
		#Check if the variable already exists no matter the scope
		
		size = 1
		if(self.search_variable_declaration(name, scope)):
			print("Variable already declared",name)
			exit()
		else:
			if(self.search_func_exist(name)):
				print("Variable already declared as a function", name)
				exit()
			# CHECK IF IT IS A NORMAL VARIABLE
			# 0 -> Normal variable
			# 1 -> Array variable
			# 2 -> Matrix variable
			types = types.upper()
			tipo = dic.datalor_translator(types)
			#Check if the rowDim and ColDim are 0 or 
			if(rowDim is None and columnDim is None or rowDim == 0 and columnDim == 0 ):	
				if(tipo == 6):
				#FOR VOID TYPE#IT DOESNT SAVE NOTHING IN MEMORY
					self.memory_num = 0
				else:
					self.memory_num = memory.assign_memory(tipo,scope,size)

				newVar = {name: { 'type': tipo, 'size': 0,'address': self.memory_num}}
				self.vars[scope]['vars'].update(newVar)
				if (tipo != 6):
					self.resources[tipo - 1] += 1
				
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
					m1 = self.add_const(m1, type(int(m1)))
					offset_end = self.add_const(int(offset), type(int(offset_end)))

					
					newVar = {name: { 'type': tipo, 'size': [[0,rowDim-1,m1,1],[0,columnDim-1,offset_end,None]],'address': self.memory_num}}
					self.vars[scope]['vars'].update(newVar)
					self.resources[tipo -1] += rowDim * columnDim

				
				#ARRAY
				else:

					self.memory_num = memory.assign_memory(tipo,scope,rowDim)
					k = self.add_const(0, type(0))
					newVar = {name: { 'type': tipo, 'size': [0,rowDim-1,k,None],'address': self.memory_num}}
					self.vars[scope]['vars'].update(newVar)
					self.resources[tipo - 1] += rowDim
		

		
			
	# Checking for sizes of the arrays and matrix to be greater than 0 
	# and not allowing the user to create for example a[0]
	def check_stype_size(self, size):
		if(size == 0):
			print('Size must be greater than 0')
			exit()

		

	#ADD PARAMS
	#It receives the name of the function and the type of the parameter

	def add_params(self, func_name, type):
		tipo = dic.datalor_translator(str(type).upper())
		self.dir_func[func_name]['params'].append(tipo)




	#Function for filling in the constants table with their values and address
	#It receives the value and the type of the constant

	def add_const(self, value, type):
		#Check if the constant already exists
		if (value not in self.constants.keys()):
		#Check if the constant is an integer value
			type = type.__name__
			if(type == 'int'):
				tipo = dic.datalor_translator('CTE_INT')
				address = memory.assign_memory(tipo,-1, 1)
				newVar = {value: {'type': tipo, 'address': address}}
				self.constants.update(newVar)
				return address
				
			else: 
				if(type == 'float'):
					tipo = dic.datalor_translator('CTE_FLOAT')
					address = memory.assign_memory(tipo,-1, 1)
					newVar = {value: {'type': tipo, 'address': address}}
					self.constants.update(newVar)
					return address
				else:
					if(type == 'str'):
						tipo = dic.datalor_translator('CTE_CHAR')
						address = memory.assign_memory(tipo,-1,1)
						newVar = {value: {'type': tipo, 'address': address}}
						self.constants.update(newVar)
						return address

		else:
			return self.constants[value]['address']
	
	
	#_______________Array calculus______________________#
	#It receives the name of the array and the scope
	#It returns the size of the array
	def get_arr_mat_info(self, name, scope): 
		if (name in self.vars[scope]['vars'].keys()):
			return self.vars[scope]['vars'][name]['size']
		else:
			#Revisa en globales
			return self.vars[0]['vars'][name]['size']

		
	#___________________________RESOURES HANDLER____________________#
	#It receives the name of the function
	#It assigns the resources to the function
	def resources_handler(self,func_name):
		#Assgin function resources
		self.dir_func[func_name]["resources"] = self.resources
		#Reset variable resource counter
		self.resources = [0,0,0,0,0]
		
	
	def print(self):
		#print(tabulate(self.vars,headers='keys'))
		#return json.dumps(self.dir_func)
		
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
	
	def get_const(self):
		return self.constants
	
	def get_func_res(self):
		main = self.dir_func['main']['resources']	
		res_global = self.dir_func['global']['resources']
		return [res_global, main]
	#GET ADDRESS FOR CREATING QUADRUPLE
	

	



