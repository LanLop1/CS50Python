#%% 1. Recoger matrícula, 2. contar carácteres 3. contar mínimo dos letras al prinicipio 4. contar números si existen al final, el número no puede empezar por 0.

matricula = input("Ingrese matrícula: ")
largo = len(matricula)
contador = 0
contador2 = 0
if largo in range(2,7):
    if matricula[0:2].isalpha():
        if matricula[1:largo+1].isalnum():
            for character in matricula:
                
                if character.isnumeric():
                    contador2 = contador2 + 1
                    print(contador2)

                    if contador2 == 1 and character == "0":
                        contador = contador + 1
                        
                        
                elif contador2 > 0 and character.isalpha():
                    contador = contador + 1
                        
            
            if contador == 0:
                print("Valid")
            else:
                print("Invalid")
        else:
            print("Invalid")
    else:
        print("Invalid")
else:
    print("Invalid")
    
# %%
