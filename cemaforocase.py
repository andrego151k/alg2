colores = ['verde', 'amarillo', 'rojo']
csemaforo = input("¿Cuál es el color del semáforo? ").lower()

match csemaforo:
    case 'verde':
        print("Siga")
    case 'amarillo':
        print("Cuidado")
    case 'rojo':
        print("Pare")
    case _:
        print("error en el color")
