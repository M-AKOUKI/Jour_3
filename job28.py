a = int(input("entrez une valeur:"))
b = int(input("entrez une 2eme valeur:"))
c = int(input("entrez une 3eme valeur:"))

if a+b>c and a+c>b and b+c>a:
    print("")
else:
    print("triangle impossible")
if  a == b and a == c and b == c:
    print("votre triangle est equilatéral")

elif a**2 + b**2 == c**2 or c**2 + b**2 == a**2 or a**2 + b**2 == b**2:
    print("votre triangle est rectangle")
    if a == b or a == c or b == c:
        print("votre triangle est isocèle")

elif a == b or a == c or b == c:
    print("votre triangle est isocèle")


else:
    print("votre triangle est quelconcque")

