import numpy as np

array = np.array([[1,2],[3,4]])
list = [[1,2],[3,4]]

print(array[0,0])
print(list[0][0])
print(array.transpose())

z = np.zeros((10,10))
print(z)
z = np.ones((10,10))
print(z)
z = np.random.random((10,10))
print(z*1001)
z = np.random.rand(10,10)
print(z*100)
print(z.mean(),z.var())

