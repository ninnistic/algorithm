T = int(input())


for tc in range(1, T+1):
    N = int(input())
    a, b, c, d, e = 0, 0, 0, 0, 0
    if N == 1:
        break
    elif N % 2 == 0:
        N /= 2
        a += 1
    elif N % 3 == 0:
        N /= 3
        b += 1
    elif N % 5 == 0:
        N /= 5
        c += 1
    elif N % 7 == 0:
        N /= 7
        d += 1
    elif N % 9 == 0:
        N /= 9
        e += 1
    print(f'#{tc} {a} {b} {c} {d} {e}')
