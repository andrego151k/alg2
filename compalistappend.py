# Inicio la lista vacía para almacenar números
numeros = []
# pido que indiquen el tamaño de lista del usuario
num_elementos = int(input("Ingrese el tamaño de la lista: "))
# pido los numeros enteros de la lista del usuario
for i in range(num_elementos):
    num = int(input("Ingrese un numero entero: "))
    numeros.append(num)
# Imprimo la lista original
print("La lista original es:", numeros)
# Inicio nuevas listas para números pares e impares
pares = []
impares = []
# Modifico la lista separando números pares e impares
for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num * 2)
# Imprimo la lista modificada
print("La lista de pares es:", pares)
print("La lista modificada es:", pares + impares)
