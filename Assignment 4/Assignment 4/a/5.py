def hIndex(citations: list) -> int:
    h = 0
    while h < len(citations) and citations[h] >= h + 1:
        h += 1
    return h


def hIndex2(citations: list) -> int:
    mn = 0
    mx = len(citations)
    h = (mx - mn) // 2
    while citations[h] > h + 1:
        if citations[h] > h + 1:
            mn = h
        if citations[h] < h + 1:
            mx = h
        h = mn + (mx - mn) // 2 + 1

    return h + 1


print(hIndex([5, 2]))  # 2
print(hIndex([10, 8, 5, 3, 3, 2]))  # 3
print(hIndex([10, 8, 5, 4, 3, 2]))  # 4
print(hIndex([100, 20, 10, 8, 5, 4, 3, 2]))  # 4
