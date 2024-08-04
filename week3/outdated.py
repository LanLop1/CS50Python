#%%
Monthdicc ={
    "January" : 1,
    "February" : 2,
    "March": 3,
    "April": 4,
    "May" : 5,
    "June" : 6,
    "July": 7 ,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def date_outdated():
    try:
        date = input("What date is is?")
        if not "," in date and any(month in date for month in Monthdicc.keys()):
            date_outdated()
        date = date.lower().title().strip()
        date = date.replace(",","")
        date = date.replace("/", " ")
        x,y,z = date.split(" ")
        x = Monthdicc.get(x,x)
        x = int(x)
        y = int(y)
        if y<32 and x<13:
            
            print(f"{z:02}-{x:02}-{y:02}")
        else:
            date_outdated()
    except ValueError:
        date_outdated()



date_outdated()
# %%

# %%
