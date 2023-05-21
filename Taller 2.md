1. Desarrollar un programa que ingrese un número entero n y separe todos los digitos que componen el número.

# Solicitamos al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: ")) 
# Creamos una lista vacía para almacenar los dígitos del número
digitos = []  

while numero > 0:  # Mientras el número sea mayor que cero
    digito = numero % 10  # Obtenemos el último dígito del número
    digitos.append(digito)  # Agregamos el dígito a la lista
    numero //= 10  # Descartamos el último dígito del número
    
# Invertimos el orden de la lista para que los dígitos queden en el orden correcto
digitos.reverse()  
# Mostramos por pantalla la lista de dígitos
print("Los dígitos del número son:", digitos)  

2. Desarrollar un programa que ingrese un número flotante n y separe su parte entera de la parte decimal, y luego entrege los digitos tanto de la parte entera como de la decimal.

numero = float(input("Ingrese un número decimal: "))
parte_entera, parte_decimal = divmod(numero, 1)
parte_entera = int(parte_entera)
parte_decimal = abs(parte_decimal)
digitos_enteros = [int(digito) for digito in str(parte_entera)]
digitos_decimales = [int(digito) for digito in str(parte_decimal)[2:]] # se omite el "0." al inicio
print("Los dígitos de la parte entera son:", digitos_enteros)
print("Los dígitos de la parte decimal son:", digitos_decimales)
16:01

3. Desarrollar un programa que permita ingresar dos números enteros y determinar si se tratan de números espejos
#Solicitamos el ingreso de los números que quiere comparar
numero1 = int(input("Introduce el primer número entero: "))
numero2 = int(input("Introduce el segundo número entero: "))

# Convertimos los números a cadenas de texto y las invertimos
cadena1 = str(numero1)
cadena2 = str(numero2)
cadena2_invertida = cadena2[::-1]

# Comparamos las cadenas invertidas
if cadena1 == cadena2_invertida:
    print("Los números son espejos")
else:
    print("Los números no son espejos")

4. Diseñar una función que permita calcular una aproximación de la función coseno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Taylor. nota: use math para traer la función coseno y mostrar la diferencia entre el valor real y la aproximación. Con cuántos valores de la serie, se tienen errores del 10%, 1%, 0.1% y 0.001%.
import math
def coseno_aproximado(x, n):
    aproximacion = 0
    for i in range(n):
        aproximacion += ((-1)**i / math.factorial(2*i)) * x**(2*i)
    return aproximacion
def terminos_para_error(error):
    n = 0
    while True:
        n += 1
        aproximacion = coseno_aproximado(x, n)
        diferencia = abs(math.cos(x) - aproximacion)
        if diferencia <= error:
            return n
x = 1.2
n_10 = terminos_para_error(0.1) # error del 10%
n_1 = terminos_para_error(0.01) # error del 1%
n_01 = terminos_para_error(0.001) # error del 0.1%
n_001 = terminos_para_error(0.00001) # error del 0.001%
print("Para un error del 10%, se necesitan", n_10, "términos")
print("Para un error del 1%, se necesitan", n_1, "términos")
print("Para un error del 0.1%, se necesitan", n_01, "términos")
print("Para un error del 0.001%, se necesitan", n_001, "términos")

5. Desarrollar un programa que permita determinar el Minimo Comun Multiplo de dos numeros enteros. Abordar el problema desde la perpectiva iterativa como recursiva.
def mcm_iterativo(a, b):
    # Encuentra el máximo de los dos números
    maximo = max(a, b)
    # Comienza un ciclo infinito
    while True:
        # Si el máximo es un múltiplo de ambos números, devuelve el máximo
        if (maximo % a == 0 and maximo % b == 0):
            return maximo
        # Si no, incrementa el máximo en 1
        maximo += 1
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
print("El Mínimo Común Múltiplo entre los dos es:")
print(mcm_iterativo(a,b))

6. Desarrollar un programa que determine si en una lista no existen elementos repetidos.

def sin_elementos_repetidos(lista):
    if len(lista) == len(set(lista)):
        return True
    else:
        return False
lista_numeros = [1, 2, 3, 4, 5]
if sin_elementos_repetidos(lista_numeros):
    print("La lista no tiene elementos repetidos")
else:
    print("La lista tiene elementos repetidos")

7. Desarrollar un programa que determine si en una lista se encuentra una cadena de caracteres con dos o más vocales. Si la cadena existe debe imprimirla y si no existe debe imprimir 'No existe'
def tiene_vocales(cadena):
    """Función que devuelve True si una cadena tiene dos o más vocales."""
    vocales = "aeiouAEIOU"  # Definimos una cadena con todas las vocales
    contador = 0  # Inicializamos un contador de vocales a cero
    for letra in cadena:  # Recorremos cada letra de la cadena
        if letra in vocales:  # Si la letra es una vocal
            contador += 1  # Incrementamos el contador de vocales
            if contador >= 2:  # Si ya hemos encontrado dos vocales
                return True  # Devolvemos True
    return False  # Si no encontramos dos vocales, devolvemos False

# Definimos una lista de cadenas
lista = ["h73p8e", "Laura", "Mundo", "Python", "Programación", ]  

encontrado = False  # Inicializamos una variable que indica si hemos encontrado la cadena buscada

for cadena in lista:  # Recorremos cada cadena de la lista
    if tiene_vocales(cadena):  # Si la cadena tiene dos o más vocales
        print("La cadena que cumple con la condición es: ", cadena)  # Mostramos la cadena por pantalla
        encontrado = True  # Indicamos que hemos encontrado la cadena buscada
        break  # Salimos del ciclo

if not encontrado:  # Si no hemos encontrado la cadena buscada
    print("No existe")  # Mostramos 'No existe' por pantalla

9. Resolver el punto 7 del taller 1 usando operaciones con vectores
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
