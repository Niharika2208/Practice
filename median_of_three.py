def median(a: int, b: int, c: int) -> int:
    if (b <= a <= c) or (c <= a <= b):
        return a
    if (a <= b <= c) or (c <= b <= a):
        return b
    else:
        return c


def median2(a: int, b: int, c: int) -> int:
    numbers = [a, b, c]
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    return numbers[1]


if __name__ == "__main__":
    print(median(25, 11, 33))
    print(median2(25, 11, 33))
