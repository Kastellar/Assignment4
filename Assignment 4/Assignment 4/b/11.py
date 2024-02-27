fib = [0, 1]
n = 10

res = list(map(lambda y: fib.append(sum(map(lambda x: fib[-x], [1, 2]))), range(2, n)))

print(fib)
