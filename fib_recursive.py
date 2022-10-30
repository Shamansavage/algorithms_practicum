import timeit
code_to_test = """
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n -2)
print(fib(35))
"""

wasted_time = timeit.timeit(code_to_test, number=1)
print(wasted_time)
