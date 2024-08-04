#%%

def main():
    frase = input("Frase para acortar: ")
    frase_twitter = shorten(frase)
    
    print (frase_twitter)


def shorten(frase):
    frase_twitter = ""
    for letra in frase:
        if not (letra == "a" or letra =="e" or letra =="i"or letra=="o" or letra=="u" or letra == "A" or letra =="E" or letra =="I"or       letra=="O" or letra=="U"):
            frase_twitter = frase_twitter + letra
    return frase_twitter


if __name__ == "__main__":
    main()
# %%
