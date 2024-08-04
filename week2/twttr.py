#%%
frase = input("Frase para acortar: ")
frase_twitter = ""
for letra in frase:
    if not (letra == "a" or letra =="e" or letra =="i"or letra=="o" or letra=="u" or letra == "A" or letra =="E" or letra =="I"or       letra=="O" or letra=="U"):
       frase_twitter = frase_twitter + letra
print (frase_twitter)

# %%
