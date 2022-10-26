'''Dadas dos listas, debes generar una tercera con todos los elementos que se repitan en ellas, pero no debe repetirse ningún elemento en la nueva lista:
lista_1 = ["h",'o','l','a',' ', 'm','u','n','d','o']
lista_2 = ["h",'o','l','a',' ', 'l','u','n','a']'''

lista_1 = ["h","o","l","a",",","m","u","n","d","o" ]
lista_2 = ["h","o","l","a"," ","l","u","n","a"]
lista_3 = []


for i, caracter in enumerate(lista_1):
    if lista_1[i] in lista_2:
        lista_3.append(caracter)

lista_3 = list(set(lista_3))
print(lista_3)
