t = int(input())
for tc in range(1, t+1):
    m, n, k = map(int, input().split()) #가로, 세로, 배추가 심어진 위치
    farm = [[0] * m for _ in range(n)]
    delta = [(0, -1), (-1, 0), (1, 0), (0, 1)]
    for _ in range(k):
        x, y = map(int, input().split()) # x= 가로 y =세로
        farm[x][y] = 1 #배추가 심어진 위치에 1박기

    # 배추농장과 똑같은 크기의 visited
    visited = [[False] * m for _ in range(n)]
    stack = []
    counts = 0


    for i in range(n):
        for j in range(m):
            # 배추밭에 1이 있고, 방문한 적이 없으면
            if farm[i][j] == 1 and not visited[i][j]:
                while True:
                    # 일단 좌표 넣어주고 True로 바꿈
                    stack.append((i, j))
                    visited[i][j] = True
                    # 그리고 그 좌표 기준으로 탐색하면서, 1인데 방문한 적이 없으면
                    # 델타를 다 돌아주고 좌표를 움직여준담에, 델타 다 돌면 깨고 +1
                    for k in delta:
                        ni = i + k[0]
                        nj = j + k[1]
                        if 0 <= ni < n and 0 <= nj < m:
                            if farm[ni][nj] == 1 and not visited[ni][nj]:
                                stack.append((ni, nj))
                                i = ni
                                j = nj
                                break
                    else:
                        if stack: #스택이 차 있으면 돌아갈 곳이 있으니까
                            v = stack.pop() #튜플 값이 나옴
                            i = v[0]
                            j = v[1]
                        else: #그게 아니고 이제 전부 다 돌았다면
                            counts += 1
                            break
    print(counts)