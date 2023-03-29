import math
encoding="utf-8"
#Zadanie1
a=pow(math.e,10)
print(a)
b=pow(math.log(5+pow(math.sin(8),2)),1/6)
print(b)
print(pow((math.log(5+(math.sin(8)*math.sin(8)))),1/6))
print(math.floor(3.55))
print(math.ceil(4.80))
#Zadanie2
imie="piotr"
nazwisko="żuryński"
print(imie.capitalize() + nazwisko.capitalize())
#Zadanie3
a=(str("la la la i jeszcze raz la"))
print(a.count("la"))
#Zadanie4
a=str("zmienna fajna jest serio")
print(a[0])
b=len(a)
print(a[b-1])
#Zadanie5
c=a.split()
print(c)
#Zadanie6
x="string"
y=float(50)
z=hex(200)
print(x)
print(y)
print(z)
print(type(x),type(y),type(z))
#Zadanie7
listasportow=["pilkanozna","siatkowka","rugby","baseball"]
aa=listasportow.reverse()
listasportow.extend(("koszykowka","atletyka"))
print(listasportow)
#Zadanie8
slownik={'np':'naprzyklad','wp':'wirtualnapolska','gg':'gadugadu'}
print(slownik)
#Zadanie9
slownikgier={'rpg':['w3','rdr2','cp2077'],'multiplayer':['lol','dota']}
print(len(slownikgier['rpg']))
#Zadanie10
wystapieniaa=input("")
print(wystapieniaa.count('a'))
#Zadanie12
listadopotegi=[1.5,2.5,3.5,5,7,9,10]
list=[]
for i in listadopotegi:
    a=(pow(i,2))
    list.append(a)

print(list)

#Zadanie13
listae=[]
ii=0
while ii<10:
    aa=int(input())
    if aa%2==0:
        listae.append(aa)
    ii+=1

print(listae)