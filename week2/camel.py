#%% 1. Comprobar si la str tiene alguna mayúscula, 2. si no la tiene no hacer nada. 3. si la string tiene mayúsculadividirla por la mayúscula 4. unir las strings restantes, convertidas en minúsculas y jantadas entre si con_ .
frase_a_convertir = input("¿Qué quieres convertir?")

for letra in frase_a_convertir:
        if letra.isupper:
            print("_" + letra.lower)
        else: 
            print(letra)
#%%




frase_a_convertir = input("¿Qué quieres convertir?")

# 1. Comprobar si la str tiene alguna mayúscula 
if not any(letra.isupper() for letra in frase_a_convertir):
    # 2. Si no la tiene, no hacer nada
    resultado = frase_a_convertir
else:
    # 3. Si la string tiene mayúscula, dividirla por la mayúscula
    # 4. Unir las strings restantes, convertidas en minúsculas y juntas entre si con _
    partes = []
    palabra = ""
    for letra in frase_a_convertir:
        if letra.isupper():
            partes.append(palabra)
            palabra = letra.lower()
        else:
            palabra += letra
    if palabra:
        partes.append(palabra)
    resultado = "_".join(partes)

print(resultado)
# %%
