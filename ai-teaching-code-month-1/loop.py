values = [1, 5, 12, 3, 12, 7, 20, 12]  # Lista de valores a evaluar
counter = 0
for value in values:      # Recorre cada elemento de la lista
    if value > 10:        # Comprueba si el valor es mayor que 10
        print("ALERT")    # Imprime ALERT si se cumple la condición
        counter = counter + 1
print(f"Hay {counter} alerts en total") 

  #Explicación línea por línea:

  #1. values = [...] — Define la lista con 8 números enteros.
  #2. for value in values: — Itera sobre la lista, asignando cada elemento a value en cada vuelta.
  #3. if value > 10: — Evalúa la condición. Solo los valores 12, 12, 20, 12 la cumplen.
  #4. print("ALERT") — Se ejecuta únicamente cuando la condición es True. Se imprime 4 veces porque hay 4 valores mayores que 10."""