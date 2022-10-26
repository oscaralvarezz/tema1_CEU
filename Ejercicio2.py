'''Realiza un programa que cumpla el siguiente algoritmo
utilizando siempre que sea posible operadores en asignación:'''

numero_magico = 123456789
numero_usuario = int(input("Escribe un número del 1 al 9: "))


def multiplication(numero_usuario):
    numero_usuario *= 9
    numero_usuario *= numero_magico

    return numero_usuario
print(multiplication(numero_usuario))

#(NO SE SI ESTÁ CORRECTO)