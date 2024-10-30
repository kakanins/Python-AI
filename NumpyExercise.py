import numpy as np #Mengimport library Numpy agar bisa digunakan
a = np.array([1,2,3,4,5]) # Membuat Numpy array 1D 
b = np.array([6,7,8,9,10])# Membuat Numpy array 1D 
c = np.array(["kevin", "jillian", 5])
print(a) # Menampilkan output dari Numpy array yang sudah dibuat
print(b) # Menampilkan output dari Numpy array yang sudah dibuat
print(c)

Array2D = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])
print(Array2D)

data = np.array([[1,2,3,4], [5,6,7,8]])
print(data.shape)
print(data[0, 3])

data = np.array([[1,2,3,4], [5,6,7,8]])
# Tambahkan code di bawah ini
print(data[:, 2])
print(data[1, :])

data = np.array([[1,2,3,4], [5,6,7,8]])
# Tambahkan code di bawah ini
print(data.diagonal(3))

empty = np.zeros((4,4), dtype="int")
print(empty)

c = np.array([3,6,9,12])
d = np.array([2,4,6,8])
print(np.add(c,d))
print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.divide(c,d))

print(c.sum(), d.sum())
print(c.min(), d.min())
print(c.max(), d.max())