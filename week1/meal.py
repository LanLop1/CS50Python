#%%
time = input("What time it is? ")


def main():

    hours, minutes = convert(time)
    if hours == 7:
        print("breakfast time")
    elif hours == 8 and minutes == 0:
        print("breakfast time")
    elif hours == 12.0:
        print("breakfast time")
    elif hours == 13 and minutes == 0:
        print("breakfast time")
    elif hours == 18:
        print("breakfast time")
    elif hours == 19 and minutes == 0:
        print("breakfast time")

def convert(time):
    hours,minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes/60
    return hours, minutes


if __name__ == "__main__":
    main()
#%%