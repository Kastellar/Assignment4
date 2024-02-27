def remove(n: int) -> int:
    lst = list(range(1, n + 1))
    a = 1
    while len(lst) > 1:
        t = []
        for i in range(a % 2, len(lst), 2):
            t.append(lst[i])
        lst = t
        a += 1
    return lst[0]


print(remove(3))
