lst1 = [i for i in range(1, 10) if i % 2]
lst2 = [i for i in range(1, 10) if i % 2 == 0]

lst = list(map(lambda x: x**2, lst1 + lst2))
print(lst)
