from functools import reduce

numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x**2, numbers))
print(squares)

numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

strings = ["apple", "banana", "cherry"]
uppercase_strings = list(map(lambda x: x.upper(), strings))
print(uppercase_strings)

strings = ["apple", "banana", "cherry", "orange", "grape"]
long_strings = list(filter(lambda x: len(x) > 5, strings))
print(long_strings)

fahrenheit_temperatures = [32, 68, 86, 104]
celsius_temperatures = list(map(lambda x: (5/9) * (x - 32), fahrenheit_temperatures))
print(celsius_temperatures)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print(prime_numbers)

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
squared_elements = list(map(lambda x, y: x**2 + y**2, list1, list2))
print(squared_elements)

strings = ["level", "radar", "hello", "world", "noon"]
palindromes = list(filter(lambda x: x == x[::-1], strings))
print(palindromes)

strings = ["apple", "banana", "cherry", "orange", "grape"]
lengths = list(map(lambda x: len(x), strings))
print(lengths)

numbers = [-1, 2, -3, 4, -5]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)

n = 10
fibonacci_numbers = reduce(lambda x, _: x + [x[-1] + x[-2]], [0] * (n-2), [0, 1])
print(fibonacci_numbers)

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

strings = ["listen", "silent", "hello", "world", "banana", "ananab"]
anagrams = list(filter(lambda x: is_anagram(x[0], x[1]), [(strings[i], strings[j]) for i in range(len(strings)) for j in range(i+1, len(strings))]))
print(anagrams)

def is_consonant_string(s):
    return all(c.lower() not in 'aeiou' for c in s)

strings = ["hello", "world", "banana", "apple", "cherry", "orange"]
consonant_strings = list(filter(lambda x: is_consonant_string(x), strings))
print(consonant_strings)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
rolling_average = list(map(lambda i: sum(numbers[i-2:i+1]) / 3, range(2, len(numbers))))
print(rolling_average)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
perfect_squares = list(filter(lambda x: int(x**0.5)**2 == x, numbers))
print(perfect_squares)
