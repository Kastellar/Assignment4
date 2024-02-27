lst = list(range(2, 100))

res = list(filter(lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)), lst))
print(res)
