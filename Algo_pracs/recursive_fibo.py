# [ 0, 1, 1, 2, 3, 5, 8, 11]
# 해당 array에 솔루션이 있다면 따로 계산할 필요 없고
# 없다면, 한번만 계산하면 된다.

fib_array = [0, 1]


def fib_recur_dp(n):
    if n < len(fib_array):
        return fib_array[n]
    else:
        fib = fib_recur_dp(n - 1) + fib_recur_dp(n - 2)
        fib_array.append(fib)
        return fib
