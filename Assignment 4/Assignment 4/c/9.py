def isGood(number: int) -> bool:
    n = str(number)
    return all(
        int(i) % 2 == 0 if index % 2 == 0 else i in ["2", "3", "5", "7"]
        for index, i in enumerate(n)
    )


def isGoodRange(n: int) -> int:
    nums = list(filter(isGood, range(10 ** (n - 1) - 1, 10**n + 1)))
    print(nums)
    return len(nums)


def isGoodRange2(n: int) -> int:
    return (5 ** (n // 2 + n % 2) * 4 ** (n // 2)) % (10**9 + 7)


# print(isGoodRange(1))
# print(isGoodRange(2))
# # print(isGoodRange(3))
# print(isGoodRange(4))

print(isGoodRange2(1))
print(isGoodRange2(2))
print(isGoodRange2(3))
print(isGoodRange2(4))
print(isGoodRange2(50))
