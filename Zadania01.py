import math
import random
#Zadanie 1

#print("komunikat 1")
#rint("komunikat 2")

#zadanie 2

#imie=input("Podaj swoje imie")
#rok_urodzenia=int(input("Podaj rok urodzenia"))

#wiek=2023-rok_urodzenia

#print(imie,",masz",wiek,"lat")

#Zadanie 3

#a=int(input("Podaj liczbe:a"))
#b=int(input("Podaj liczbe b"))

#suma=a+b
#roznica=a-b
#iloczyn=a*b
#iloraz=a/b
#pierwiastek=math.sqrt(a+b)
#potegaa=pow(a,b)
#potegab=pow(b,a)
#print(suma,roznica,iloczyn,iloraz,pierwiastek,potegaa,potegab,sep='\n')

#Zadanie 4

#r=int(input("Podaj promien"))
#if r<0 or r==0:
   # print("Zle dane")
#else:
   # pole_kola=math.pi*(r*r)
   # obwod_kola=2*math.pi*r
    #print("Pole kola:",pole_kola)
   # print("Obwod kola:",obwod_kola)

#Zadanie 5
#a=float(input("Podaj a"))
#b=float(input("Podaj b"))
#c=float(input("Podaj c"))

#delta=pow(b,2)-4*a*c
#if delta>0:
 #   x1=(-b-math.sqrt(delta))/(2*a)
  #  x2=(-b+math.sqrt(delta))/(2*a)
   # print(x1,x2,sep="\n")
#elif delta==0:
 #   x1 = (-b - math.sqrt(delta)) / (2 * a)
  #  print(x1)
#else:
 #   print("brak rozwiazan")

#Zadanie 6

#los=random.randint(0,11)
#count=0
#wynik=0
#while wynik !=los:
 #   count+=1
  #  wynik=int(input())
   # if wynik>los:
    #    print("za duzo")
    #elif wynik<los:
     #   print("za malo")
    #else:
     #   print("Zgadles za ",count)

#Zadanie 7
#n=int(input("Podaj liczbe naturalna"))

#i=0
#j=n+2
#for i in range(n+1):
 #   j-=1
  #  print(i,j-1)

#Zadanie 8
#nie wiem co to szereg maclaurina

#Zadanie 9
#n=input("Podaj liczbe n")
#print("Liczba cyfr w tym ",len(n))
#suma=0
#for cyfra in n:
 #   suma+=int(cyfra)

#print(suma)

#Zadanie 10

#lista=[]
#for i in range(5):
 #   a=random.uniform(-1,1)
  #  lista.append(a)
   # i+=1
#print(lista)
#for i, elem in enumerate(lista):
 #   print(f"lista[{i}]:{elem}")

#print(len(lista))
#m=max(lista)
#me=lista.index(m)

#print(m,me)

