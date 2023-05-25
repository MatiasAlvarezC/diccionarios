""""
Calculadora de Estadísticas de Números
Escribe un programa que permita al usuario ingresar una lista de números y realice los siguientes cálculos estadísticos:
1. Calcular la suma de los números.
2. Calcular el promedio de los números.
3. Encontrar el número mínimo y el número máximo de la lista.
4. Calcular la desviación estándar de los números.
El programa debe solicitar al usuario que ingrese la lista de números separados por espacios y luego imprimir los resultados de los cálculos estadísticos.
"""
import statistics
numeros = input("Ingrese una lista de numeros separados por espacios: ")

numeros_lista = numeros.split()  # separa los numeros ingresados por el usuario

suma = 0
promedio = 0
con = 0
minimo = 0
mayor = 0
desviacion_estandar = 0 

for numeros in numeros_lista:
    suma += float(numeros)    #sumar numeros 
    con += 1   #contador para calcular promedio
promedio = suma / con

numeros_lista = [float(numero) for numero in numeros_lista]  #convierte los numeros de la lista en enteros para poder hacer la desviacion, minimo y maximo

desviacion_estandar = statistics.stdev(numeros_lista)
minimo = min(numeros_lista)
mayor = max(numeros_lista) 

print("Los numeros ingresados son: " , numeros_lista)
print("--------------------------------------------------")
print("La suma de los números ingresados es:", suma)
print("El promedio de los números ingresados es:", promedio)
print("El menor de los números ingresados es:", minimo)
print("El mayor de los números ingresados es:", mayor)
print("El desviacion estandar de los números ingresados es:", desviacion_estandar)