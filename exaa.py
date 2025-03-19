print("gust the word !!!")

t = 0
word = ["a", "m", "i", "n", "e"]
win = []

while True :
    n = input("enter the later :").lower()
    if n == "a":
        win.insert(0, "a")
        print("ok: a----")
    elif n == "m":
        win.insert(1, "m")
        print("ok: -m---")
    elif n == "i":
        win.insert(2, "i")
        print("ok: --i--")
    elif n == "n":
        win.insert(3, "n")
        print("ok: ---n-")
    elif n == "e":
        win.insert(4, "e")
        print(f"ok: ----e")        
    else:
        print("noooop")
    t = t + 1

    if win == ['a', 'm', 'i', 'n', 'e']:
        print("wineeeer  you are not dying today !! ")
        break 
    elif t == 10 :
        print("mooot lfa9ira ta3t mok !!")
        break