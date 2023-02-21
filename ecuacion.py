import numpy as np

A = np.array([[2, 3], [4, 5]])

B = np.array([6, 7])

X = np.linalg.solve(A, B)

print("La solución es:", X)