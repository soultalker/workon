import time


t = time.perf_counter()
for i in range(100, 1000):
    a = int(i/100)
    b = int((i - a * 100)/10)
    c = i - a*100 - b * 10
    if i == a**3 + b**3 + c**3:
        print(i)
print(time.perf_counter() - t)


t = time.perf_counter()
for i in range(100, 1000):
    temp = list(str(i))
    if i == int(temp[0]) ** 3 + int(temp[1]) ** 3 + int(temp[2]) ** 3:
        print(i)
print(time.perf_counter() - t)
