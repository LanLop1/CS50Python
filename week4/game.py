#%%
import random

def randad():
    while True:
        try:
            n = int(input("Level: "))
            if n < 1:
                print("Please enter a positive integer.")
                continue
            return random.randint(1, n)
        except ValueError:
            print("Invalid input. Please enter an integer.")

adivina = randad()

def game():
    while True:
        try:
            intento = int(input("Guess: "))
            if intento < adivina:
                print("Too small!")
            elif intento > adivina:
                print("Too large!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

game()

# %%
