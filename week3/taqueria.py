#%%

felipes = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def pedirtacos():
    total = 0
    while True:
        try:
            taco = input("What taco do you want?")
            taco = taco.lower().title()
            x = felipes.get(taco,"")
            x= float(x)
            total = total + x
            print(f"${total:.2f}")
        except EOFError:
            break
        except ValueError:
            pass

pedirtacos()

# %%
