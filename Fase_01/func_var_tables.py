# # ------------------------------------------------------------
# # DATALOR: DICTIONARIES - VARIABLES TABLE
# # Mariana Favarony Avila -A01704671
# # Mario Juarez - A01411049
# #  
# # ------------------------------------------------------------
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
		
	#VARIABLES
	# CHECK IF THE VARIABLE ALREADY EXISTS IN THE SCOPE 
	def search_variable(self, name,scope):
		if (name in self.vars[scope]['vars'].keys()):
			return True
		else:
			return False
	
	#ADD VARIABLES
	def add_vars(self, name, scope, type, rowDim = None, columnDim = None):
		#Check if the variable already exists no matter the scope
		if(self.search_variable(name, scope)):
			print("Variable already declared",name)
			exit()
		else:
			# CHECK IF IT IS A NORMAL VARIABLE
			# 0 -> Normal variable
			# 1 -> Array variable
			# 2 -> Matrix variable

			#Check if the rowDim and ColDim are 0 or 
			if(rowDim is None and columnDim is None or rowDim == 0 and columnDim == 0 ):
				newVar = {name: { 'type': type, 'size': 0,'address': ''}}
				self.vars[scope]['vars'].update(newVar)
				print(self.vars.values())
			else:
				# MATRIX
				if(rowDim != 0 and columnDim != 0):
					newVar = {name: { 'type': type, 'size': [rowDim,columnDim],'address': ''}}
					self.vars[scope]['vars'].update(newVar)
					print(self.vars.values())
				
				#ARRAY
				else:
					newVar = {name: { 'type': type, 'size': [rowDim],'address': ''}}
					self.vars[scope]['vars'].update(newVar)
					print(self.vars.values())
					
			
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


