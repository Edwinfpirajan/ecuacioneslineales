import numpy as np

a11 = float(input("Ingrese el coeficiente a11: "))
a12 = float(input("Ingrese el coeficiente a12: "))
a21 = float(input("Ingrese el coeficiente a21: "))
a22 = float(input("Ingrese el coeficiente a22: "))
b1 = float(input("Ingrese el término independiente b1: "))
b2 = float(input("Ingrese el término independiente b2: "))

A = np.array([[a11, a12], [a21, a22]])

B = np.array([b1, b2])

X = np.linalg.solve(A, B)

print("La solución es:", X)