t = int(input())
for tc in range(1, t+1):
    n = float(input())
    max_length = 13
    answer = ''

    while n and max_length:
        if n * 2 >= 1:
            answer += '1'
            n = n *2 -1
        else:
            answer += '0'
            n = n * 2
        if n == 0:
            break
    else:
        answer = 'overflow'
    print(f"#{tc} {answer}")