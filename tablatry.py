# Mostrar la tabla de multiplicar del 4
# Iterar sobre los números del 1 al 10
numero = input("inserte un numero para las tablas")
 for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")