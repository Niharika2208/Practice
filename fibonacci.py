"""
fib1(5) = fib1(3) + fib1(4)
        = fib1(1) + fib1(2) + fib1(2) + fib1(3)
        = 1 + fib1(0) + fib1(1) + fib1(0) + fib1(1) + fib1(1) + fib1(2)
        = 1 + 0 + 1+ 0 + 1 + 1 + fib1(0) + fib1(1)
        = 4 + 0 + 1
        = 5


"""

number_recursive_calls = 0


def fib1(n: int) -> int:
    global number_recursive_calls
    number_recursive_calls += 1

    if n == 0 or n == 1:
        return n
    else:
        return fib1(n-2) + fib1(n-1)


def fib_series():
    for i in range( 16):
        print(fib1(i))


def fib2(n: int) -> int:
    a = 0
    b = 1
    count = 0
    while n >= 0:
        number_loop += 1
        c = a + b
        a = b
        b = c
        n -= 1
    return a, count


if __name__ == "__main__":
    print(fib1(2))
    print("Recursive calls - ", number_recursive_calls)
    fib_series()
    print(fib2(23))


