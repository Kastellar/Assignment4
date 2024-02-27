def isListPalindrome(lst: list) -> bool:
    return lst == lst[::-1]


print(isListPalindrome([1, 2, 2, 1]))
print(isListPalindrome([1, 2]))
