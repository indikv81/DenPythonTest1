import numpy as np

ar1 = np.linspace(0, 2, 9)
print(ar1)

def f1(i, j):
    return (i + 1) * (j + 1)

print(np.fromfunction(f1, (10, 10), dtype=np.int))

print(np.arange(0, 3000, 2))
