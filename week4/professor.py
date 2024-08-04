#%%
import random

def main():
    contador_fallos = 0
    contador_try = 0
    level = get_level()
    while True:
        x, y = generate_integer(level)
        respuesta = x + y
        contadorciclo = 0
        while contadorciclo < 3:
            try:
                intento = int(input(f"{x} + {y} = "))
                if intento == respuesta:
                    contador_try += 1
                    break
                else:
                    contadorciclo += 1
                    print("EEE")
                    if contadorciclo == 3:
                        contador_fallos += 1
                        contador_try += 1
                        print(respuesta)
            except ValueError:
                contadorciclo += 1
                print("EEE")
                if contadorciclo == 3:
                    contador_fallos += 1
                    contador_try += 1
                    print(respuesta)
        if contador_try == 10:
            print(f"{10 - contador_fallos}")
            break

def get_level():
    while True:
        level = input("Ingrese un nivel del 1 al 3: ")
        if level in ["1", "2", "3"]:
            return int(level)
        print("Nivel inválido. Por favor, ingrese 1, 2 o 3.")

def generate_integer(level):
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    return x, y
if __name__ == "__main__":
    main()