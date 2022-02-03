import numpy as np

print('a1')
a1 = np.array([1, 2, 3, 4, 5, 6])
print(a1.ndim)
print(type(a1))
print(a1)
print(a1.shape)

# Arrays (ndarray) aus range erzeugen
print('a2')
a2 = np.arange(6)
print(type(a2))
print(a2)
print(a2.shape)

# Dimension hinzufügen
print('a3')
a3 = a2[np.newaxis, :]
print(a3.shape)
print(a3)
print(a3.ndim)
print(np.sum(a3))

# Reshape
print('reshape')
a4 = np.arange(20).reshape(4, 5)
print(a4)
print(a4.shape)
print(a4.ndim)
print(np.sum(a4))
print(np.sum(a4[0]))
print(a4.sum(axis=0))
print(a4.sum(axis=1))
print(a4.cumsum(axis=1))

print('linspace')
li = np.linspace(0, np.pi, 10)
print(type(li))
print(li)
print(li.shape)

print('zeros')
z = np.zeros((3, 3))
print(z)

print('ones')
z = np.ones((3, 3))
print(z)
