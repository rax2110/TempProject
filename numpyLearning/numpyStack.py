import numpy as np
from datetime import datetime

a = np.random.rand(100)
b = np.random.rand(100)
T = 100000

def slow_dot_product(a,b):
    sum = 0
    for e,f in zip(a,b):
        sum += e*f
    return sum


t0 = datetime.now()
for t in range(T):
    slow_dot_product(a,b)
dt1 = datetime.now() - t0

t0 = datetime.now()
for t in range(T):
    a.dot(b)
dt2 = datetime.now() - t0

print("dt1 / dt2",dt1.total_seconds()/dt2.total_seconds()) 