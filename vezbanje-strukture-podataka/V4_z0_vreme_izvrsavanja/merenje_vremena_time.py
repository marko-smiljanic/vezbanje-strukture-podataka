from time import time, perf_counter

#moze i sa perf_counter() ... mora i import

start = time() 

for i in range(1000):
    rez = i**2
    print(rez)

rez = None
print(rez)


end = time()
print(end - start)