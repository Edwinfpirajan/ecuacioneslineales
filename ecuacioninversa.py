import numpy as np

# Solicitar al usuario los coeficientes y términos independientes de las ecuaciones
a11 = float(input("Ingrese el coeficiente a11: "))
a12 = float(input("Ingrese el coeficiente a12: "))
a21 = float(input("Ingrese el coeficiente a21: "))
a22 = float(input("Ingrese el coeficiente a22: "))
b1 = float(input("Ingrese el término independiente b1: "))
b2 = float(input("Ingrese el término independiente b2: "))

# Definir los coeficientes de las ecuaciones en una matriz
A = np.array([[a11, a12], [a21, a22]])

# Calcular la matriz inversa de A
A_inv = np.linalg.inv(A)

# Definir los términos independientes en un vector
B = np.array([b1, b2])

# Resolver el sistema de ecuaciones lineales utilizando la matriz inversa
X = np.dot(A_inv, B)

# Imprimir la solución
print("La solución es:", X)