fib_array = [0, 1]


def fib(n: int):
    for i in range(2, n + 1):
        fib_array.append(fib_array[i - 1] + fib_array[i - 2])
    return fib_array[-1]


if __name__ == "__main__":
    result = fib(100)
    print(f"{result:,}")
