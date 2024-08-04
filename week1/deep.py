#%% trying to make a match case for each of the examples asked for
cuestion = "What is the Answer to the Great Question of Life, the Universe, and Everything?"
answer = input(cuestion).strip().lower()
match answer:
    case "42":
        print("Yes")
    case "forty-two":
        print("Yes")
    case "forty two":
        print("Yes")
    case _:
        print("No")

# %%
