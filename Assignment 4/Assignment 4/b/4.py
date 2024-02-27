from string import ascii_lowercase

lst = [ascii_lowercase[:i] for i in range(1, 10)]
new_lst = list(filter(lambda x: len(x) >= 5, lst))

print(lst)
print(new_lst)
