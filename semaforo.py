colores = ['verde', 'amrillo', 'rojo',]
csemaforo = str(input("cual es el color del semaforo ")).lower()
for icolor in colores:
    if csemaforo == "verde":
        print("siga")
    elif csemaforo == "amarillo":
          print("cuidado")
    elif csemaforo == 'rojo':
          print("pare")
