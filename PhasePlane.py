# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 17:35:10 2020

@author: nicol
"""
import numpy as np
import matplotlib.pyplot as plt

def f(Y, t):
    y1, y2 = Y
    return [5*y2, -y1]

y1 = np.linspace(-4.0, 4.0, 20)
y2 = np.linspace(-4.0, 4.0, 20)

Y1, Y2 = np.meshgrid(y1, y2)

t = 0

u, v = np.zeros(Y1.shape), np.zeros(Y2.shape)

NI, NJ = Y1.shape

for i in range(NI):
    for j in range(NJ):
        x = Y1[i, j]
        y = Y2[i, j]
        yprime = f([x, y], t)
        u[i,j] = yprime[0]
        v[i,j] = yprime[1]
     

Q = plt.quiver(Y1, Y2, u, v, color='r')


plt.xlabel('$y_1$')
plt.ylabel('$y_2$')
plt.xlim([-4, 4])
plt.ylim([-4, 4])
plt.show()

# =============================================================================
# plt.savefig('images/phase-portrait.png')
# =============================================================================

















