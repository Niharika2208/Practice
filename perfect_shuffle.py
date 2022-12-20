def interleave(a: list[int], b: list[int]) -> list[int]:
    temp_list = []
    shuffle_list = []
    for temp in b:
        temp_list.append(temp)
    # print(temp_list)
    for i in a:
        shuffle_list.append(i)

        for j in temp_list:
            shuffle_list.append(j)
            temp_list.remove(j)
            break
    return shuffle_list


def perfect_shuffle(a: list[int]) -> list[int]:
    split: int = int(len(a) / 2)
    first = a[:split]
    second = a[split:]
    return interleave(first, second)


def shuffle_number(a: int) -> int:
    random_list = []
    count = 1
    for i in range(a):
        random_list.append(i)
    random_temp = perfect_shuffle(random_list)
    while random_list != random_temp:
        random_temp = perfect_shuffle(random_temp)
        count += 1
        if random_temp == random_list:
            return count
    return count


if __name__ == "__main__":
    print(interleave([4, 2, 5], [9, 8, 1]))
    print(perfect_shuffle([7, 3, 8, 2, 6, 10]))
    print(shuffle_number(52))
