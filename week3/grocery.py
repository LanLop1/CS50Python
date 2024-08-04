
lista_compra = []
lista_compra_printed = []





def listacompra():
    
    while True:
        try:
            compra = input("")
            compra = compra.upper()
            lista_compra.append(compra)

        except EOFError:
            lista_compra.sort()
            for item in lista_compra:
                if item not in lista_compra_printed:
                    n_en_lista = lista_compra.count(item)
                    lista_compra_printed.append(item)
                    print(n_en_lista, item)
            break
        except ValueError:
            pass

listacompra()