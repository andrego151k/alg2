numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []  # Lista de pares
impares = []  # Lista de impares

for num in numeros:  # Bucle para cada número
    if num % 2 == 0:  # Comprobar si es par
        pares.append(num)  # Agregar a pares
    else:  # Si es impar
        impares.append(num)  # Agregar a impares
        impares.append(num * 2)  # Duplicar y agregar

if impares:  # Si hay impares
    print("Lista de impares y duplicados:", impares)  # Imprimir impares
else:  # Si no hay impares
    print("No hay impares.")

if pares:  # Si hay pares
    print("Lista de pares:", pares)  # Imprimir pares
else:  # Si no hay pares
    print("No hay pares.")
