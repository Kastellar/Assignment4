lst = list(range(100))

new_lst = list(filter(lambda x: int(x**0.5) == x**0.5, lst))

print(new_lst)
