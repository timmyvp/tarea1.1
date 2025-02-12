import numpy as np


epsilon = 1.0
iteracion = 0
while 1.0 + epsilon != 1.0:
    epsilon /= 2
    iteracion = iteracion + 1
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")

epsilon *= 2
print(f"Precisión de máquina: {epsilon}")
