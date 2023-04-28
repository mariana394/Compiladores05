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
		if (name in self.vars[scope].values()):
			return True
		else:
			return False
	
	#ADD VARIABLES
	def add_vars(self, name, scope, type):
		#Check if the variable already exists no matter the scope
		if(self.search_variable(name, scope)):
			print("Variable already declared")
			exit()
		else:
			newVar = {name: { 'type': type, 'address': ''}}
			self.vars[scope]['vars'].update(newVar)
			
		#print(self.vars[scope]['vars'].keys())	
		#print(self.vars[scope]['vars'].values())	

	#ADD PARAMS
	def add_params(self, func_name, type):
		
		self.dir_func[func_name]['params'].append(type)
		#print(self.dir_func.values())


