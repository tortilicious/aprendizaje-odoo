def pares_hasta(n):
    for num in range(1, n + 1):
        if num % 2 == 0:
            yield num

for num in pares_hasta(10):
    print(num)
