import numpy as np

list = [1,2,3]

array = np.array([1,2,3])

for e in list:
    print(e)

for e in array:
    print(e)

list.append(4)
print(list)
list = list + [5]
print(list)

list2 = []
for e in list:
    list2.append(e + e)
print(list2)

print(array + array)
print(2*array)
print(2*list)
print(array**2)
print(np.sqrt(array))