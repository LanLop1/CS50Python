#%% python si al preguntar por greetings la persona responde con hello, recibe 0$, si empieza por h pero no es hello gana 20$, qualquier otra respuesta recibe 100$

ask_greetings = input("greetings")
letra = "h"
if ask_greetings == "hello":
    print("0$")
elif ask_greetings.startswith(letra):
    print("20$")
else:
    print("100$")

# %%
