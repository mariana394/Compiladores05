# ------------------------------------------------------------
# DATALOR: SPECIAL FUNCTIONS
# Mariana Favarony Avila -A01704671
# Mario Juarez - A01411049
# FILE WITH THE INFORMATION OF ALL SPECIAL FUNCTIONS
# ------------------------------------------------------------

class special_functions:
    
    def __init__(self):
        
        self.special_func = {
                        "exploration" : {'params': [5,1],},
                        "financial_state": {'params':[5,5,3,3],},
                        "dummi_regression": {'params':[5,3],},
                        "season_analysis": {'params':[5],},
                        "trend_prediction": {'params':[5],},
                        "model_predict": {'params':[5,5],},
                        }

    #Function to search and check parameters of special functions
    def search_sf_param(self,func_name, param, tipo):
        if(func_name in self.special_func.keys()):
            list_param = self.special_func[func_name]['params']
            if(len(list_param) < param):
                print("ERROR: TOO MANY PARAMETERS", len(list_param), " " , param)
                exit()
            else: 
                if(list_param[param - 1] != tipo):
                    print("ERROR: TYPE MISTMATCH")
                    exit()

        else:
            print("ERROR: NOT A SPECIAL FUNCTION")
            exit()

    