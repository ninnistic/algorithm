def cabbage(y, x):
    q = [(y, x)]
    farm[y][x] = 0  # 방문한 곳을 0으로 만들어버리고 델타탐색 해주기
    delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]

    while q:
        y, x = q.pop(0)
        for d in delta:  # 기준을 중심으로 델타탐색 해주고, 만약 1이있다면 0으로 만들어버림
            ny = y + d[0]
            nx = x + d[1]
            if 0 <= ny < n and 0 <= nx < m:
                if farm[ny][nx] == 1:
                    farm[ny][nx] = 0
                    q.append((ny, nx))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())  # 가로, 세로, 배추가 심어진 위치
    farm = [[0] * m for _ in range(n)]
    counts = 0

    for _ in range(k):
        a, b = map(int, input().split())  # a = 가로 b = 세로
        farm[b][a] = 1  # 배추가 심어진 위치에 1박기

    for j in range(n):
        for i in range(m):
            if farm[j][i] == 1:  # 만약 배추가 있다면
                cabbage(j, i)  # 한 좌표 기준 델타탐색이 다 끝나면(0처리를 다 해버리면)
                counts += 1

    print(counts)
