#%%
from pyfiglet import Figlet
import sys
figlet = Figlet()

if len(sys.argv) == 2:
    sys.exit("Invalid usage")
elif len(sys.argv) > 4:
    sys.exit("Invalid usage")
for arg2 in sys.argv[2:]:
    if sys.argv[1] == "-f" or sys.argv[1] == "-font":
        figlet.setFont(font=arg2)
    else: sys.exit("Invalid usage")

texto_transformar = input()

print(figlet.renderText(texto_transformar))

# %%
