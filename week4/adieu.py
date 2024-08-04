import inflect

# Crear una instancia del motor inflect
p = inflect.engine()
Nombres = []

def adieu():
    while True:
        try:
            nom = input("")
            Nombres.append(nom)
        except EOFError:
            imprimir = p.join(Nombres)
            print(f"Adieu, adieu, to {imprimir}")
            break

adieu()