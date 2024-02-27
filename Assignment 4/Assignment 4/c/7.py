def swap(l: list) -> list:
    for i in range(0, len(l) - 1, 2):
        l[i], l[i + 1] = l[i + 1], l[i]
    return l


lst = [1, 2, 3, 4]
print(swap(lst))
