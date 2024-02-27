from math import log10


def numToWord(n: int) -> str:
    t = [n // 10**i % 10 for i in range(int(log10(n) + 1))]
    print(t)


numToWord(1000)
numToWord(634)
numToWord(64565454)
