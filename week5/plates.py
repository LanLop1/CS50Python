#%% 1. Recoger matrícula, 2. contar carácteres 3. contar mínimo dos letras al prinicipio 4. contar números si existen al final, el número no puede empezar por 0.
def main():
    matricula = str(input("Ingrese matrícula: "))
    is_valid(matricula)


def is_valid(s):
    largo = len(s)
    contador = 0
    contador2 = 0
    if largo in range(2,7):
        if s[0:2].isalpha():
            if s[1:largo+1].isalnum():
                for character in s:
                    
                    if character.isnumeric():
                        contador2 = contador2 + 1
                        print(contador2)

                        if contador2 == 1 and character == "0":
                            contador = contador + 1
                            
                            
                    elif contador2 > 0 and character.isalpha():
                        contador = contador + 1
                            
                
                if contador == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
    



    
# %%
