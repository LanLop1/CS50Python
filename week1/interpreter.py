#%% hacemos un imput de la operacion, dividimos la operacion para elejir las variables y con un if else en funcion del símbolo elegido, python hace la operación
input_math = input("Operation: ")
x, y, z = input_math.split(" ")
x = float(x)
z = float(z)
if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print (x * z)
elif y == "/":
    print(x / z)
else:
    print("sintax error")




# %%
