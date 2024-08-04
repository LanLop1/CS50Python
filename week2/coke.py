# 1. Pedir el tipo de moneda que mete, solo hacepta 10, 5 y 25.
# 2. Cada vez que meta la moneda tiene que sumar la cantidad a la anterior y devolver el valor total.
# 3. Si el valor total supera 50  le resta 50 y el resultado sale como change:

#%%
def maquina_de_cocacola():
    moneda = int(input("insert a coin"))
    dinero = 0
    if moneda == 5 or moneda == 10 or moneda == 25:
        dinero += moneda
        print(str(dinero) + "moneda")
        if dinero > 50:
            dinero - 50
            print(str(dinero) + "cambio")
        maquina_de_cocacola()
    else:
        maquina_de_cocacola()
maquina_de_cocacola()
# %% máquina funcional
def maquina_de_cocacola():
    dinero = 0
    while dinero < 50:
        moneda = int(input("insert a coin"))
        if moneda == 5 or moneda == 10 or moneda == 25:
            dinero += moneda
            print("Amount Due: " + str(50 - dinero))
        else:
            print("no se acepta esta moneda")
    if dinero >= 50:
        dinero = dinero - 50
        print("Change Owed: " + str(dinero))

maquina_de_cocacola()
# %%
