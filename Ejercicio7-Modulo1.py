# 7. Una mosca sigue una trayectoria de modo que x = t cos(ωt) e y = t**2 sin(ωt) en
# coordenadas cartesianas. Grafique y como función de x para 100 valores de
# 0 ≤ t ≤ 10. En el mismo gráfico, marque con puntos rojos la posición de la mosca
# cuando t sea entero.

"""Primero importamos las bibliotecas necesarias."""
import matplotlib.pyplot as plt
import numpy as np

"""Ahora definiremos las funciones x e y."""
def x(t, omega):
    return t * np.cos(omega*t)

def y(t, omega):
    return t**2 *np.sin(omega*t)


"""Aqui definiremos t, que ira de un intervalo de 1 al 10. Tambien definiremos omega."""
"""Usaremos linspace para que el intervalo de 1 a 1 lo recorra en 100 puntos"""
t_valor = np.linspace(1, 11, 100)
omega = 2*np.pi


"""Luego, evaluaremos las funciones x e y con los valores t y omega bien definidos anteriormente. """
x_valor = x(t_valor, omega)
y_valor = y(t_valor, omega)


"""Graficaremos la trayectoria de la mosca con plt.plot"""
plt.plot(x(t_valor, omega), y(t_valor, omega), label= 'Trayectoria de la mosca')


"""Definiremos un t_entero con un for en un rago de 1 al 10, osea, recorrera todos los valores enteros entre el 1 y 10"""
for t_entero in range(11):
    plt.scatter(x(t_entero, omega), y(t_entero, omega), color='red')

"""Personalizaremos un poco el grafico nombrando los ejes y colocando un grid() que es una casilla"""
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
