#%% El programa recibe una extension .algo y devuelve el formato web /img/png como ejemplo

ext_input = input("name of the tipe: ").strip().lower()

if ext_input.endswith(".gif"):
        print("image/gif")
elif ext_input.endswith(".jpg"):
        print("image/jpeg")
elif ext_input.endswith(".jpeg"):
        print("image/jpeg")
elif ext_input.endswith(".png"):
        print("image/png")
elif ext_input.endswith(".pdf"):
        print("application/pdf")
elif ext_input.endswith(".txt"):
        print("text/plain")
elif ext_input.endswith(".zip"):
        print("application/zip")
else:
        print("application/octet-stream")
# %%

