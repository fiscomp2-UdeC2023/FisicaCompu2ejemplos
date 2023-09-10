def factorial(num):
    """Calcula el factorial de un número."""
    if num == 0:
        return 1
    return num * factorial(num - 1)

def coeficiente_binomial(n, k):
    """Calcula el coeficiente binomial C(n, k)."""
    return factorial(n) // (factorial(k) * factorial(n - k))

def triangulo_pascal(n):
    """Imprime el Triángulo de Pascal hasta la fila n."""
    for i in range(n + 1):
        for j in range(i + 1):
            print(coeficiente_binomial(i, j), end=" ")
        print()  # Cambio de línea al final de cada fila

# Ejemplo para imprimir el Triángulo de Pascal hasta la fila 5
n = 20
triangulo_pascal(n)
