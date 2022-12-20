def prime_twins(n: int) -> list[tuple[int, int]]:
    a = []
    b = []
    twin_list = []

    for prime_list in range(pow(n + 2, 2)):
        if prime_list > 2:
            for j in range(2, prime_list):
                if (prime_list % j) == 0:
                    break
            else:
                a.append(prime_list)

    for k in range(len(a) - 1):
        if a[k] == a[k + 1] - 2:
            b.append((a[k], a[k + 1]))

    for twin in range(0, n):
        twin_list.append(b[twin])

    return twin_list


def prime_triplets(n: int) -> list[tuple[int, int, int]]:
    a = []
    b = []
    triplet_list = []
    for prime_list in range(pow(n + 5, 3)):
        if prime_list > 2:
            for j in range(2, prime_list):
                if (prime_list % j) == 0:
                    break
            else:
                a.append(prime_list)

    for i in range(len(a) - 2):
        if (a[i] == a[i + 1] - 2 or a[i] == a[i + 1] - 4) and a[i] == a[i + 2] - 6:
            b.append((a[i], a[i + 1], a[i + 2]))

    for triplet in range(0, n):
        triplet_list.append(b[triplet])

    return triplet_list


if __name__ == "__main__":
    print(prime_twins(5))
    print(prime_triplets(1))
