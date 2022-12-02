"""
Different ways to clear a list in Python
"""


# def clearing(array: list[int]):
#     array.clear()
#     return array

# def clearing1(array: list[int]):
#     del array[:]
#     return array


def clearing2(array: list[int]):
    while len(array) != 0:
        array.pop()
    return array


if __name__ == "__main__":
    array = [5, 9, 1, 8, 3, 9]
    # print(clearing(array))
    # print(clearing1(array))
    print(clearing2(array))
