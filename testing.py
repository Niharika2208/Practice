def merge_sort(array: list[int]) -> list[int]:
    array_list = []
    for array_element in range(len(array)):
        array_list.append(array_element)
    return ms(array_list)


def ms(array_list: list[int]) -> list[int]:
    """Sorts `array` with merge-sort"""
    if len(array_list) > 1:
        left = array_list[: len(array_list) // 2]
        right = array_list[len(array_list) // 2:]
        merge_sort(left)
        merge_sort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                array_list[k] = left[i]
                i += 1
                k += 1
            else:
                array_list[k] = right[j]
                j += 1
                k += 1

        while i < len(left):
            array_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            array_list[k] = right[j]
            j += 1
            k += 1
    return array_list
    # raise NotImplementedError() # TODO: Add implementation


if __name__ == "__main__":
    array = [3, 2, 4, 1, 5]
    # array = [0,1,2,3,4,5]
    sorting = merge_sort(array)
    print(sorting)

    # assert array == [1, 2, 3, 4, 5]