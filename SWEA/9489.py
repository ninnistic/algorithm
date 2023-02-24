def counting(arr):
    max_v = 2
    for i in arr:
        counts = 0
        for j in i:
            if j == '1':
                counts += 1
                if counts > max_v:
                    max_v = counts
            else:
                counts = 0
    return max_v


t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    board = [input().split() for _ in range(n)]
    board_t = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            board_t[i][j] = board[j][i]

    across = counting(board)
    down = counting(board_t)

    print(f"#{tc}", across if across > down else down)
