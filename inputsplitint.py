def main():
  # Solicitar al usuario ingresar la lista
  elementos = input("Ingrese los elementos de la lista separados por espacios: ")

  # Dividir cadena 
  lista_elems = elementos.split()
  # Convertir cada elemento a int
  lista_elems = [int(elemento) for elemento in lista_elems]

  lista_duplicada = [elemento * 2 for elemento in lista_elems]
  print("La lista resultante con elementos duplicados es:", lista_duplicada)

if __name__ == "__main__":
  main()
  
