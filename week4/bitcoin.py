#%%

import sys
import requests

if len(sys.argv) == 2 and sys.argv[1].isnumeric:
    try:
        cantidad_bitcoins = float(sys.argv [1])
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        respuesta= r.json()
        rate = respuesta["bpi"]["USD"]["rate"]
        rate = float(rate.replace(",", ""))
        precio = cantidad_bitcoins*rate
        print(f"${precio:,.4f}")

    except requests.RequestException:
        print("not found")
elif not sys.argv[1].isnumeric:
    print("Command-line argument is not a number")
else:
    print("Missing command-line argument ")
    sys.exit()




# %%
