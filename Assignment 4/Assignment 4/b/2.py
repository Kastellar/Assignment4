lst = list(range(100))

new_lst = list(filter(lambda x: x % 2 == 0, lst))

print(lst, new_lst, sep="\n")
