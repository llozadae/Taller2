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