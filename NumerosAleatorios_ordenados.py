import random
import time

def generar_numeros():
    tabla_hash = {}
    for i in range(1000000):
        numero = random.randint(-10000000, 10000000)
        if numero in tabla_hash:
            tabla_hash[numero] += 1
        else:
            tabla_hash[numero] = 1
    
    with open("numeros.txt", "w") as f:
        for numero, cantidad in tabla_hash.items():
            f.write(f"{numero}\n" * cantidad)
    
    print("Se han generado los números aleatorios y se han almacenado en el archivo 'numeros.txt'.")

def ordenar_numeros():
    with open("numeros.txt", "r") as f:
        numeros = [int(linea) for linea in f]
    
    print("Seleccione el método de ordenamiento:")
    print("1. Burbuja")
    print("2. Shell")
    print("3. Inserción")
    opcion = int(input("> "))
    
    if opcion == 1:
        start_time = time.time()
        for i in range(len(numeros)):
            for j in range(i+1, len(numeros)):
                if numeros[i] > numeros[j]:
                    numeros[i], numeros[j] = numeros[j], numeros[i]
        end_time = time.time()
        nombre_metodo = "Burbuja"
    elif opcion == 2:
        start_time = time.time()
        n = len(numeros)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = numeros[i]
                j = i
                while j >= gap and numeros[j - gap] > temp:
                    numeros[j] = numeros[j - gap]
                    j -= gap
                numeros[j] = temp
            gap //= 2
        end_time = time.time()
        nombre_metodo = "Shell"
    elif opcion == 3:
        start_time = time.time()
        for i in range(1, len(numeros)):
            valor_actual = numeros[i]
            posicion = i
            while posicion > 0 and numeros[posicion - 1] > valor_actual:
                numeros[posicion] = numeros[posicion - 1]
                posicion = posicion - 1
            numeros[posicion] = valor_actual
        end_time = time.time()
        nombre_metodo = "Inserción"
    else:
        print("Opción no válida.")
        return
    
    with open(f"numeros_{nombre_metodo.lower()}.txt", "w") as f:
        for numero in numeros:
            f.write(f"{numero}\n")
    
    tiempo_total = end_time - start_time
    print(f"Se han ordenado los números y se han almacenado en el archivo 'numeros_{nombre_metodo.lower()}.txt'.")
    print(f"El tiempo de ejecución del método de ordenamiento {nombre_metodo} fue de {tiempo_total} segundos.")

while True:
    print("Seleccione una opción:")
    print("1. Generar números aleatorios")
    print("2. Ordenar números")
    print("3. Salir")
    opcion = int(input("> "))
    
    if opcion == 1:
        generar_numeros()
    elif opcion == 2:
        ordenar_numeros()
    elif opcion == 3:
        break
    else:
        print("Opción no válida.")
