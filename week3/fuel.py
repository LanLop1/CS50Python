#%%

def main():
    gasofa = input("¿Cuanta gasolina te queda?")
    porcentage = deposito(gasofa)
    porcentage = int(round(porcentage, 0))
    if 99 <= porcentage <=100:
        print("F")
    elif 0 <= porcentage <=1:
        print("E")
    elif porcentage >100:
        main()
        
    else:
        print(str(porcentage) + "%")
def deposito(gasofa):
    try:
        x,y = gasofa.split("/")
        x = int(x)
        y = int(y)
        z=  x/y*100
        return z
    except ValueError:
        main()
    except ZeroDivisionError:
        main()
main()

# %%
