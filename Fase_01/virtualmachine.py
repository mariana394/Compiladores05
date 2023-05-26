# -----------------------------------------------------------
# DATALOR: Virtual Machine
# Mariana Favarony Avila A01704671
# Mario Juarez  A01411049
# Virtual Machine....
# -----------------------------------------------------------


        
#IMPORT
code = open("intermedio.txt", "r")

components = code.read().split("&&")



# assign 3 parts of the code
quad = components[0]
dirFunc = components[1]
constants = components[2]

#Split quad everu line break
quad = quad.split("\n")
#Cast dirFunc as a Dictionary
dirFunc = eval(dirFunc)
#Cast constants as a Dictionary
constants = eval(constants)

#print quad 1 by 1 with an index
for i in range(len(quad)):
    print(i, quad[i])
