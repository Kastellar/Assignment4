def fib(n: int) -> int:
    lst = [0, 1]
    if n <= 1:
        return lst[n]

    for i in range(2, n + 1):
        lst.append(lst[i - 1] + lst[i - 2])
    return lst[n]


print(fib(3))
