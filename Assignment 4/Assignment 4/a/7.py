def getSquares(n: int):
    res = n
    for j in range(2, int(n**0.5 + 1)):
        i = n // j**2
        r = n % j**2
        res = min(res, i + getSquares(r))
    return res


def getSquares2(n: int):
    mx = 1000000000
    d = [mx] * (n + 1)
    d[0] = 0
    for i in range(1, n + 1):
        t = mx
        for j in range(1, int(i**0.5) + 1):
            t = min(t, d[i - j * j] + 1)
        d[i] = t
    return d[n]


print(getSquares2(124435))
