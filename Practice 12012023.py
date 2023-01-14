"""
Write a function that takes two integers as arguments and returns the sum of the integers.
"""

# def addition(a: int, b: int) -> int:
#     return a + b
#
#
# if __name__ == "__main__":
#     print(addition(5, 6))

"""
Write a function that takes a list of numbers as an argument and returns the average of the numbers in the list.
"""

# def average(array: list[int]) -> float:
#     add = 0
#     for i in array:
#         add = add + i
#     return add / len(array)
#
#
# if __name__ == "__main__":
#     print(average([4, 6, 9, 10, 4, 8, 2]))

"""
Write a function that takes a string as an argument and returns the number of vowels in the string.
"""

# def vowels(word: str) -> int:
#     count1 = 0
#     for vowel in word:
#         if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u':
#             count1 += 1
#     return count1
#
#
# if __name__ == "__main__":
#     print(vowels("elephant"))

"""Write a function that takes a list of strings as an argument and returns a new list that contains only the strings 
that have a length greater than 5. """

# def strings(words: list[str]) -> list[str]:
#     new_list = []
#     for word in words:
#         if len(word) > 5:
#             new_list.append(word)
#     return new_list
#
#
# if __name__ == "__main__":
#     print(strings(["Niharika", "Ramya", "Henry", "Dhanush"]))

"""Write a function that takes a dictionary as an argument and returns the key-value pairs in alphabetical order by 
the key. """

# def dictionary(Word: dict[str]) -> dict[str]:
#     Words = sorted(Word.items())
#     return Words
#
#
# if __name__ == "__main__":
#     print(dictionary({'firstname:': 'Niharika', 'id': '3456', 'place': 'Bengaluru'}))

"""
Write a function that takes a list of numbers as an argument and returns the second largest number in the list.
"""

# def second(array: list):
#     large = max(array)
#     array.remove(large)
#     return max(array)
#
#
# if __name__ == "__main__":
#     print(second([3, 4, 10, 76, 342]))


"""Write a function that takes a number as an argument and returns true if the number is a prime number, 
and false otherwise. """

# def prime(n: int) -> bool:
#     if n <= 1:
#         return False
#     else:
#         for i in range(2, n):
#             if n % i == 0:
#                 return False
#
#         return True
#
#
# def next_prime(n: int) -> int:
#     while prime(n) is False:
#         for i in range(2, n):
#             if n % i == 0:
#                 n += 1
#         return n
#
#
# if __name__ == "__main__":
#     print(prime(4))
#     print(next_prime(9))


"""
Write a function that takes a list of numbers as an argument and returns the median of the numbers.
"""

# def median(array: list) -> float:
#     sorted_array = sorted(array)
#     print(sorted_array)
#     if len(sorted_array) % 2 != 0:
#         med = len(sorted_array) // 2
#         return sorted_array[med]
#     else:
#         med = len(sorted_array) // 2
#         print(sorted_array[med])
#         print(sorted_array[med - 1])
#         return (sorted_array[med - 1] + sorted_array[med]) / 2
#
#
# if __name__ == "__main__":
#     print(median([3, 13, 2, 34, 11, 17, 27, 47]))


"""Write a function that takes two strings as arguments and returns true if they are anagrams of each other, 
and false otherwise. """

# def anagrams(a: str, b: str):
#     str1 = sorted(a)
#     str2 = sorted(b)
#     if str1 == str2:
#         return True
#     else:
#         return False
#
#
# if __name__ == "__main__":
#     print(anagrams("listen", "silents"))

"""
Write a function that takes a list of integers as an argument and returns the sum of all the even numbers in the list.
"""

# def even(array: list[int]):
#     temp = []
#     add = 0
#     for i in array:
#         if i % 2 == 0:
#             temp.append(i)
#
#     for j in temp:
#         add = add + j
#
#     return add
#
#
# if __name__ == "__main__":
#     print(even([3, 5, 9, 13]))


"""Write a program that takes a list of integers and an integer value as arguments, and returns the index of the 
first occurrence of the value in the list. If the value is not found, the program should return -1. """

# def occurrence(array: list[int], n: int):
#     if n in array:
#         return array.index(n)
#     else:
#         return -1
#
#
# if __name__ == "__main__":
#     print(occurrence([3, 3, 4, 5, 9, 3], 3))


"""
Write a program that takes a list of integers as an argument and returns the list in reverse order.
"""

# def reverse(array: list):
#     return array[::-1]
#
#
# if __name__ == "__main__":
#     print(reverse([3, 4, 5, 1, 10]))


"""
Write a function that takes a list of integers as an argument and returns the number of unique integers in the list.
"""

# def unique(array: list):
#     un = len(set(array))
#     return un
#
#
# if __name__ == "__main__":
#     print(unique([3, 4, 5, 2, 10, 4]))


"""Write a program that takes a list of integers and a target value as arguments, and returns the indices of all 
elements in the list that are equal to the target value.
"""


# def ind(array: list, n: int) -> int:
#     temp = []
#     for i in range(len(array)):
#         if array[i] == n:
#             temp.append(i)
#     return temp
#
#
# if __name__ == "__main__":
#     print(ind([3, 4, 4, 10], 4))

"""Write a function that takes a list of integers and a value as arguments and returns a new list with all the 
elements from the original list that are less than the given value. """


# def compare(array: list, n: int) -> list:
#     less = []
#     for i in range(len(array)):
#         if array[i] < n:
#             less.append(array[i])
#     return less
#
#
# if __name__ == "__main__":
#     print(compare([3, 10, 7, 12, 8], 8))

"""
Write a program that takes a list of integers as an argument and returns a new list with all duplicates removed.
"""


# def duplicate(array: list) -> list:
#     return set(array)
#
#
# if __name__ == "__main__":
#     print(duplicate([3, 10, 7, 3, 5, 9, 10]))


