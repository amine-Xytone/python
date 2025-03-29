# en general il y a 4 types des fonctions 
# 1 .
def hello ():
    print("helllo mr how are you !")

hello()


# 2 .
def hello_2 (nom):
    print(f"hello mr {nom} how are you !")

hello_2("amine")


# 3.
def avec_rutourn_pas_dargument() :
    a = 1
    b = 3 
    c = a + b
 
# 4.
def avec_rutourn_dargument(a,b) :
    c = a + b
    return c


def somme (a , b):
    c = a  + b
    return c

a = float(input ("entre la valure de a : "))
b = float(input ("entre la valure de b : "))
print((f"a + b = {somme(a,b)}"))


def somme (a , b):
    c = a + b
    print(f"a + b {c}")

a = float(input ("entre la valure de a : "))
b = float(input ("entre la valure de b : "))
somme (a,b)