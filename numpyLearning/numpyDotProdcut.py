import numpy as np

a = np.array([1,2])

b = np.array([2,1])
dot = 0
for e,f in zip(a,b):
    dot += e*f

print(dot)
print(a*b)
print(np.sum(a*b))
print(np.dot(a,b))
print(a.dot(b))

a_mag = np.sqrt((a*a).sum())
print(a_mag)
a_mag = np.linalg.norm(a)
print(a_mag)
b_mag = np.linalg.norm(b)
print(b_mag)
cosangle = a.dot(b) / (a_mag*b_mag)
print(cosangle)
angle = np.arccos(cosangle)
print(angle)