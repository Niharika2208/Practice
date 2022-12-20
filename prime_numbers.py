def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    else:
        for i in range(2, n):
            if (n % i) == 0:
                return False

        return True


def next_prime(n: int) -> int:
    if n <= 1:
        return 2
    isprime = False
    while not isprime:
        isprime = True
        for i in range(2, n):
            if n % i == 0:
                n += 1
                isprime = False
                break
    return n


if __name__ == "__main__":
    print(is_prime(4))
    print(next_prime(4))
