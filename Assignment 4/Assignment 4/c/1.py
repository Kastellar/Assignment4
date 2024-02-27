from math import log


def isPowerOfFour(n: int) -> bool:
    t = log(n, 4)
    return t == int(t)


n = int(input())

print(isPowerOfFour(n))
