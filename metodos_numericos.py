import numpy as np


epsilon = 1.0
iteracion = 0
while 1.0 + epsilon != 1.0:
    epsilon /= 2
    iteracion = iteracion + 1
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")

epsilon *= 2
print(f"Precisión de máquina: {epsilon}")

import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = np.pi
N_values = [10, 100, 1000, 10000]
errors_abs = []
errors_rel = []

for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    print(f"N={N}: Error absoluto={error_abs}, Error relativo={error_rel}")

plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de pi')
plt.show()

def calcular_errores(x, y, valor_real):
    diferencia = x - y
    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100
    print(f"Diferencia: {diferencia}")
    print(f"Error absoluto: {error_abs}")
    print(f"Error relativo: {error_rel}")
    print(f"Error porcentual: {error_pct}%")
    return error_abs, error_rel

valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)]

for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    calcular_errores(x, y, real)