strings = [
    "radar",
    "level",
    "noon",
    "civic",
    "deified",
    "apple",
    "banana",
    "orange",
    "grape",
    "mango",
    "car",
    "house",
    "table",
    "chair",
    "dog",
    "cat",
    "fish",
    "bird",
    "sun",
    "moon",
]
lst = list(filter(lambda x: x == x[::-1], strings))
print(lst)
