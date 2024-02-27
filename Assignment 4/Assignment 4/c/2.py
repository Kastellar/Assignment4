def link(lst1: list, lst2: list) -> list:
    p1, p2 = 0, 0
    res = []
    for _ in range(len(lst1) + len(lst2)):
        if len(lst1) <= p1:
            res.extend(lst2[p2:])
            break
        if len(lst2) <= p2:
            res.extend(lst1[p1:])
            break

        if lst1[p1] <= lst2[p2]:
            res.append(lst1[p1])
            p1 += 1
        elif lst1[p1] > lst2[p2]:
            res.append(lst2[p2])
            p2 += 1
    return res


print(link([1, 2, 4, 5, 6, 7], [1, 3, 4]))
