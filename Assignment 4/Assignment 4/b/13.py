strings = [
    "hello",
    "world",
    "python",
    "programming",
    "apple",
    "banana",
    "sky",
    "aaaa",
    "bbbb",
]

lst = list(filter(lambda x: all(i not in x for i in "aeiouAEIOU"), strings))

print(lst)
