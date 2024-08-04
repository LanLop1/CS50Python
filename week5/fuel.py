#%%
def main():
    gasofa = input("¿Cuanta gasolina te queda?")
    porcentage = convert(gasofa)
    gauge(porcentage)
    
    


def convert(fraction):
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        z=  x/y*100
        if x>y:
            return ValueError
        else:
            z = int(round(z, 0))
            
            return z
    except ValueError:
        return ValueError
    except ZeroDivisionError:
        return ZeroDivisionError


def gauge(percentage):
    if 99 <= percentage <=100:
        
        return "F"
    elif 0 <= percentage <=1:
        
        return "E"
    elif percentage >100:
        main()
        
    else:
        
        return (str(percentage) + "%")


if __name__ == "__main__":
    main()