import numpy as np

a1 = np.array([1, 2, 3, 4, 5, 6])
print(type(a1))
print(a1)
print(a1.shape)

# Arrays (ndarray) aus range erzeugen
a2 = np.arange(6)
print(type(a2))
print(a2)
print(a2.shape)

# Dimension hinzufügen
a3 = a2[np.newaxis, :]
print(a3.shape)
print(a3)

li = np.linspace(0, 10, 10)
print(type(li))
print(li)
print(li.shape)
