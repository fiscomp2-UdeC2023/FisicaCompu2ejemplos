import numpy as np
from scipy.special import erf

f = lambda x:np.exp(-x**2)

# intervalos
a, b = 0, 1
dx = b-a
# Integral exacta
exacto = 0.5*np.sqrt(np.pi)*(erf(b)-erf(a))

print(exacto)

# regla punto medio 
punto_medio = dx * f(0.5*(b+a))

# regla del trapezoide 
trapezoide = 0.5 * dx * (f(a) + f(b))

# regla de simpson
simpson = (dx/6.0) * (f(a) + f(b) + 4*f(0.5*(b+a)))

print(f'integral exacta = {exacto}')
print(f'punto medio = {punto_medio}')
print(f'trapezoide = {trapezoide}')
print(f'regla de simpson = {simpson}')