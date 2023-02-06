# 피보나치 수

n = int(input())


def fib(n):
    if n <= 1:
        return n  # 0이거나 1이거나
    else:
        return fib(n-1) + fib(n-2)


print(fib(n))
