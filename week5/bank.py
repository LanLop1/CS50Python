#%% python si al preguntar por greetings la persona responde con hello, recibe 0$, si empieza por h pero no es hello gana 20$, qualquier otra respuesta recibe 100$
def main():
    ask_greetings = input("greetings")
    value(ask_greetings)


def value(greeting):
    letra = "h"
    hola = "hello"
    if greeting.split()[0]== hola:
        return 0
    elif greeting.startswith(letra):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()



# %%
