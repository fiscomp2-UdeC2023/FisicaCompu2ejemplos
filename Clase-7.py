import numpy as np
def f(x):
    return x**3

# se definen los limites:
a ,b = 1, 5

# se define el numero de puntos:
N = 5
dx = (b-a)/(N-1) # porque son 4 rectangulos.

suma = 0.0

for i in range(N):
    print(suma)
    suma += f(a + i * dx) * dx
    print(suma)

# se le suma 1 menos ya que es un cuadrito
# menos de los puntos totales.
suma = np.sum(f(np.linspace(a, b, N-1, endpoint=False))*dx)
# suma = np.sum(f(np.arange(a, b, (b-a)/(N-1))*dx ) es lo ismo


print(f"Integral de x**3 entre a= {a} y b = {b}")
print(f"integral numerica {suma}")
# es la integral de x**3 que es 1/4 por x**4:
print(f"integral exacta: {0.25*(b**4 - a**4)}")