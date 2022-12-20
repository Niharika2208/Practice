import random


def create_random(n: int) -> list[int]:
    random_int: list = [random.randint(5, 99) for num in range(n)]
    return random_int


def to_string(a: list[int]) -> str:
    a_temp = ",".join(str(number) for number in a)
    return a_temp


def pos_min(a: list[int]) -> int:
    a_min: int = a.index(min(a))
    return a_min


def swap(a: list[int]) -> None:
    a_temp = a[0]
    a[0] = a[len(a) - 1]
    a[len(a) - 1] = a_temp


if __name__ == "__main__":
    print(create_random(9))
    print(to_string([2, 4, 6, 8]))
    print(pos_min([8, 0, 0]))
    swap([9, 7, 4, 6])
