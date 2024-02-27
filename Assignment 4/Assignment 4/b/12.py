strings = ["listen", "silent", "heart", "earth", "bat", "tab", "stop", "top"]

lst = list(
    filter(
        lambda x: sorted(x[0]) == sorted(x[1]),
        [
            (strings[l1], strings[l2])
            for l1 in range(0, len(strings) - 1)
            for l2 in range(l1 + 1, len(strings))
        ],
    )
)

print(lst)
