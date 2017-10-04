import numpy as np
import time, collections

numbers = list(np.random.randint(100000, size=5000))
# print(numbers)
numbers2 = numbers[:]

t = time.time()
e = []
o = []
while len(numbers) >0:
    n = numbers.pop()
    if n%2 ==0:
        e.append(n)
    else:
        o.append(n)
print(time.time() - t)

t = time.time()
even = [n for n in numbers2 if n%2 == 0]
odd = [n for n in numbers2 if n%2 != 0]
print(time.time() - t)

print(collections.Counter(e) == collections.Counter(even) and collections.Counter(o) == collections.Counter(odd) )
# print(e, even)
# print(o, odd)
