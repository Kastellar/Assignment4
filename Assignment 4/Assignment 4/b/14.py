numbers = [10, 5, 9, 11, 10, 12, 11, 10, 9, 12, 11, 10, 11]

lst = list(
    map(
        lambda x: round((x[0] + x[1] + x[2]) / 3, 2),
        [numbers[i : i + 3] for i in range(len(numbers) - 2)],
    )
)

print(lst)
