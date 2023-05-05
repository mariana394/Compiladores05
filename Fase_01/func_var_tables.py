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
				"params": []
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
		
	#FUNCIONES
	# Function for adding functions to function directory
	def add_function(self, name, scope, type):
		#SEARCHING IF THE FUNCTION ALREADY EXISTS
		if(name in self.dir_func.keys()):
			print("Function " + name + " already declared")
			exit()
		else:
			self.dir_func[name] = {}
			self.dir_func[name]["return_type"] = type
			self.dir_func[name]["scope"] = scope
			self.dir_func[name]["params"] = []
			
			#CREATING VARIABLE TABLE FOR THE FUNCTION SCOPE
			self.vars[scope] = {}
			self.vars[scope]['function_name'] = name
			self.vars[scope]['vars'] = {}

			#print(self.dir_func.keys(), self.dir_func.values())
		
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
			return True
		else:
			if (name in self.vars[0]['vars'].keys()):
				return True
			else:
				print('Variable not declared')
				exit()
		
	
	#_________________CREATING VARIABLES_________________
	#ADD VARIABLES
	def add_vars(self, name, scope, type, rowDim = None, columnDim = None):
		#Check if the variable already exists no matter the scope
		type = type.upper()
		if(self.search_variable_declaration(name, scope)):
			print("Variable already declared",name)
			exit()
		else:
			# CHECK IF IT IS A NORMAL VARIABLE
			# 0 -> Normal variable
			# 1 -> Array variable
			# 2 -> Matrix variable

			#Check if the rowDim and ColDim are 0 or 
			if(rowDim is None and columnDim is None or rowDim == 0 and columnDim == 0 ):
				tipo = dic.datalor_translator(type)
				newVar = {name: { 'type': tipo, 'size': 0,'address': memory.assign_memory(tipo,scope)}}
				self.vars[scope]['vars'].update(newVar)
				#print(self.vars.values())
			else:
				# MATRIX
				if(rowDim != 0 and columnDim != 0):
					tipo = dic.datalor_translator(type)
					newVar = {name: { 'type': tipo, 'size': [rowDim,columnDim],'address': memory.assign_memory(tipo,scope)}}
					self.vars[scope]['vars'].update(newVar)
					#print(self.vars.values())
				
				#ARRAY
				else:
					tipo = dic.datalor_translator(type)
					newVar = {name: { 'type': tipo, 'size': [rowDim],'address': memory.assign_memory(tipo,scope)}}
					self.vars[scope]['vars'].update(newVar)
					#print(self.vars.values())
					
			
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
				newVar = {value: {'type': tipo, 'address': memory.assign_memory(tipo,-1)}}
				self.constants.update(newVar)
			else: 
				if(type == 'float'):
					tipo = dic.datalor_translator('CTE_FLOAT')
					newVar = {value: {'type': tipo, 'address': memory.assign_memory(tipo,-1)}}
					self.constants.update(newVar)
				# else:
				# 	if(type == 'str'):
				# 		tipo = dic.datalor_translator('CTE_CHAR')
				# 		newVar = {value: {'type': tipo, 'address': memory.assign_memory(tipo,-1)}}
				# 		self.constants.update(newVar)

			
			# print(self.constants.keys())
			# print(self.constants.values())

	
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
	#GET ADDRESS FOR CREATING QUADRUPLE
	#def get_address(self, item, scope):

	



