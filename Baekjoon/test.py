

def collatz(n):
    # if 1이라면 return 0
    steps = 0
    if n == 1:
        return 0

    # if 짝수라면
    if n % 2 == 0:
        steps = collatz(n // 2)
        steps += 1
    else:
        steps = collatz(n * 3 + 1)
        steps += 1

    if steps > 500:
        return -1

    return steps


print(collatz(16))
