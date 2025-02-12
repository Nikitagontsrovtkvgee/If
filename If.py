#Näidis 1
from random import *
from random import randint
arv=randint(0, 10)
print(arv)
if arv>5:
    print("***************") 
    print(f"Arv {arv} suurem kui 5")
    print("***************")
if arv>5: print(f"Arv {arv} suurem kui 5");

#Näidis 2
arv=randint(-10, 10)
if arv>0:
    print("Positiivne")
else:
    print("Negatiivne") #viga!

if arv>0:
    print("Positiivne")
elif arv==0:
    print("0")
else:
    print("Negatiivne")

nimi=input("Mis on sinu nimi?")
if nimi.isupper() and nimi.lower()=="juku":
    print("Lähme kinno")
    try:
        age=int(input("Kui vana sa oled?"))
        if age<6:
            pilet="Tasuta"
        elif age<=14:
            pilet="Lastepilet"
        elif age<=65:
            pilet="Täispilet"
        elif age<=100:
            pilet="Soodupilet"
        print(pilet)
    except Exception as e:
        print("Tekkis viga: ",e)
else:
    print("Ei minna")