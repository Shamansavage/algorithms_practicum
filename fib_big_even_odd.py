def fib_eo(n):
    lst = [0, 1] + [x for x in range(1, n + 1)]
    for i in lst[3:]:
        lst[i] = (lst[i-1] + lst[i-2]) % 10
    return lst[n]

def isEven(n):
    return ('even', 'odd')[n%2]
def main():
    n = int(input())
    print(isEven(n))


if __name__ == "__main__":
    main()
