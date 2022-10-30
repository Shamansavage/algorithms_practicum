def fib(n):
    if n in {0, 1}:
        return n
    fib1, fib2 = 0, 1
    for _ in range(2, n + 1):
        fib1, fib2 = fib2, fib1 + fib2

    return fib2
if __name__ == '__main__':
    n = input("Номер элемента fib: ")
    n = int(n)
    print(fib(n))