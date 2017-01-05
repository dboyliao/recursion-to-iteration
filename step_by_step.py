# step 0: naive implementation
def fib(n):

    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)


# step 1: partition the function into base-case logic and incremental logic
def step1_fib(n):

    if n < 2:
        return 1

    return step1_incre(n)

def step1_incre(n):

    return step1_fib(n-1) + step1_fib(n-2)
