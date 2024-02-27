lst = [15, 12, 9, 7, 16, 13, 9, 12, 0, 6, 11]

new_lst = list(map(lambda x: round(5 / 9 * (x - 32), 2), lst))

print(lst)
print(new_lst)
