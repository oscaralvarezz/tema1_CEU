import sys

if sys.argv[1].isnumeric()==False:
    print("El valor que se ha introducido no es un número entero positivo")
    sys.exit()

numeros = []
for i in sys.argv[1]:
    numeros.append(i)
for j in range (0, len(numeros)):
    numeros[j] = int(numeros[j])

#ahora invertimos la lista de números
numeros = numeros[::-1]

numero_final = "{:0"+str(len(numeros))+"d}"
for i, numero in enumerate(numeros):
    if i ==0:
        print(numero_final.format(numeros[i]))
    else:
        formatear = numeros[i]*(10**i)
        print(numero_final.format(formatear))