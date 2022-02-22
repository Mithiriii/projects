var_x = 10
password = "My super secret password"

source = '__import__("os").getcwd()'

# globals = globals().copy()
# del globals['password']
# print(globals)

globals = {}

result = eval(source, globals)
print(result)

#print(globals())