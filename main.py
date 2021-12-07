#visual studio code

import numpy as np #matematiksel islemler icin matris vb
from scipy.optimize  import linprog #optimize modulundeki linear programming fonksiyonlari
import matplotlib.pyplot as plt

''' z = x1 + 2x2 max
x1 + 3x2 <= 3       y = (3 - x1) / 3
2x1 + x2 <= 2       y = 2 - 2x1
3x1 + x2 <= 3       y = 3 - 3x1
x1, x2 >= 0 '''

#kisit degiskenleri
A = np.array([[1, 3], [2, 1], [3, 1]])
b = np.array([3, 2, 3])
c = np.array([-1, -2]) #max dedigi icin z denklemindeki katsayilar - ile carpilir

#<= upperbound, = equality
result = linprog(c = c, A_ub = A, b_ub = b, method = 'simplex', bounds = (0, None))

print(result.fun)
print(result.x)

X = np.linspace(0, 10, 10)
y1 = (3 - X) / 3
y2 = 2 - 2 * X
y3 = 3 - 3 * X

#grafik cizimi
plt.plot(X, y1, label = "x1 + 3x2 <= 3")
plt.plot(X, y2, label = "2x1 + x2 <= 2 ")
plt.plot(X, y3, label = "3x1 + x2 <= 3")
plt.scatter(result.x[0], result.x[1])
plt.legend()
plt.xlabel("x1")
plt.ylabel("x2")
plt.xlim(left = 0)
plt.ylim(bottom = 0, top = 10)
plt.show()

