def sine(a,b) :
    if a >= 0 and b >= 0 :
        print("meme signe !")
    else :
        print ("mo mr defirant signe !")

def min (a,b):
    if a >= b :
        mi = b
    else :
        mi = a
    return mi


def max (a,b) :
    if a >= b :
         mx = a
    else :
        mx = b
    return mx
    
a =float(input("entre la valure da A :"))
b =float(input("entre la valure de B :"))
sine(a,b)
print(f"la valur maximum est {max(a,b)}")
print(min(a,b))