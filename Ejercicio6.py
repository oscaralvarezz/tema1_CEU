'''Realiza una función separar(lista) que tome una lista
de números enteros y devuelva dos listas ordenadas.
La primera con los números pares y la segunda con los números impares.'''

impares = []
pares = []

def separar(lista):
    for number in range(len(lista)):
        
        if lista[number]%2==0:
            valores_pares = lista[number]
            pares.append(valores_pares)
        else:
            valores_impares = lista[number]
            impares.append(valores_impares)

separar([6,7,3,2,4,8,10,9,1,11,13])
print("Los valores impares son:",impares)
print("Los valores pares son:",pares)
