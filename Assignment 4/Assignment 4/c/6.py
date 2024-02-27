def sumLists(l1: list, l2: list) -> list:
    res = [0 for i in range(max(len(l1), len(l2)))]
    for i in range(min(len(l1), len(l2))):
        res[i] += l1[i] + l2[i]
        if res[i] >= 10:
            res[i] -= 10
            res[i + 1] += 1
    if len(l1) != len(l2):
        for i in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
            t = l1 if len(l1) > len(l2) else l2
            res[i] += t[i]
    return res


print(sumLists([2, 4, 3], [5, 6, 4, 0]))
