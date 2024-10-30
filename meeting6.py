import numpy as np #Importing the Numpy library so that it can be used

empty = np.zeros((4,4), dtype="int")
print(empty)
empty[0, 1:4] = [1,55,3]
print(empty)
empty[-1, 0] = 7 #-1 = row index terakhir
print(empty) # ^ 
             # | new value
empty[1:3, 1] = [9,5]
print(empty)   # ^
               # | New value
empty[2:4, 2:4] = [0,70], [14,22]
print(empty)

a = np.array([[1,2,3,4,5],[6,7,8,9,10]]) # Create a 1D Numpy array
b = np.array([6,7,8,9,10])# Create a 1D Numpy array
print(a.shape) # Displays the output of the Numpy array that has been created
print(b.shape) # Displays the output of the Numpy array that has been created

array3D = np.array([[[1,2,3], [4,5,6]],
[[7,8,9], [10,11,12]],
[[13,14,15], [16,17,18]]])

print(array3D.shape)

data = np.array([[1,2,3,4], [5,6,7,8]])
print(data.shape)
print(data[1, 2])

data = np.array([[1,2,3,4], [5,6,7,8]])
# Add the code below
print(data[:, 1:4])

data = np.array([[1,2,3,4], [5,6,7,8]])
# Tambahkan code di bawah ini
print(data.diagonal(-1))

c = np.array([3,6,9,12])
d = np.array([2,4,6,8])
print(np.add(c,d))
print(np.subtract(c,d))
print(np.multiply(c,d))
print(np.divide(c,d))