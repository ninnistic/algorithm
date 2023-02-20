t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split())
    top_down = [[9] * (m+2)]
    left_right = [[9] + list(map(int, input().split())) + [9] for _ in range(n)]
    board = top_down + left_right + top_down
    res = 0
    delta = [(-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)] # 우하좌상

    for i in range(0, n+1): # 1부터 n+1까지인거 명심...예를들어서 n이 3이라면 우린 0,1,2,
        for j in range(0, m+1): # 제로 패딩 했으니까 범위...꼬옥 챙겨...!
            counts = 0
            for k in delta:
                nx = i + k[0]
                ny = j + k[1]
                if board[i][j] > board[nx][ny]:
                    counts += 1
                    if counts >= 4:
                        res += 1
                        break

    print(f"#{tc} {res}")


