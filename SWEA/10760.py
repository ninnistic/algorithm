t = int(input())

for tc in range(1,t+1):
    n, m = map(int, input().split())
    top_down = [9] * (m+2)
    # n = dx (세로)  m = dy (가로)
    # top_down은 2차원 배열 안으로 들어가므로, 리스트에 넣어줌.
    board = [top_down] + [[9] + list(map(int, input().split())) + [9] for _ in range(n)] + [top_down]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]   # 오른쪽부터 시계방향으로 ->
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    res = 0
    for j in range(1, n+1):
        for k in range(1, m+1):
            counts = 0
            for i in range(8):
                nx = j + dx[i] # 0
                ny = k + dy[i] # 1
                if board[j][k] > board[nx][ny]:
                    counts += 1
                    if counts >= 4:
                        res += 1
                        break
    print(f"#{tc} {res}")











