#!/usr/bin/env python-sirius

import numpy as np
import matplotlib.pyplot as plt


lista_t = []
lista_x = []

t = 0
x = 0
print(f't:{t:09.6f} x:{x:+09.3f}')

lista_t.append(t)
lista_x.append(x)

dt = 0.001  # [s]
while t < 6:
    # x = x + 2 * t * dt
    x = x + dt*np.sqrt(1-x**2)
    t = t + dt
    lista_t.append(t)
    lista_x.append(x)
    print(f't:{t:09.6f} x:{x:+09.3f}')


te = np.linspace(0, 6, 1000)
xe = np.sin(te)

plt.plot(te, xe, label='exact')
plt.plot(lista_t, lista_x, '-', label='RK')
plt.legend()
plt.show()


