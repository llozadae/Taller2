import math

numeros = []

for i in range(5):
    numero = float(input("Introduce el número {}: ".format(i+1)))
    numeros.append(numero)

# Promedio
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)

# Mediana
numeros_ordenados = sorted(numeros)
if len(numeros_ordenados) % 2 == 0:
    mediana = (numeros_ordenados[len(numeros_ordenados)//2-1] + numeros_ordenados[len(numeros_ordenados)//2]) / 2
else:
    mediana = numeros_ordenados[len(numeros_ordenados)//2]
print("La mediana es:", mediana)

# Promedio multiplicativo
producto = 1
for numero in numeros:
    producto *= numero
promedio_multiplicativo = math.pow(producto, 1/len(numeros))
print("El promedio multiplicativo es:", promedio_multiplicativo)

# Orden ascendente
numeros_ascendentes = sorted(numeros)
print("Los números ordenados de forma ascendente son:", numeros_ascendentes)

# Orden descendente
numeros_descendentes = sorted(numeros, reverse=True)
print("Los números ordenados de forma descendente son:", numeros_descendentes)

# Potencia del mayor número elevado al menor número
mayor = max(numeros)
menor = min(numeros)
potencia = math.pow(mayor, menor)
print("La potencia del mayor número elevado al menor número es:", potencia)

# Raíz cúbica del menor número
raiz_cubica = math.pow(menor, 1/3)
print("La raíz cúbica del menor número es:", raiz_cubica)