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