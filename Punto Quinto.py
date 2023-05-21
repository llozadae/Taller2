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