t = int(input())

for tc in range(1, t + 1):
    v, e = map(int, input().split())
    board = [[0] * (v + 1) for _ in range(v + 1)]

    visited = [False] * (v + 1)
    stack = []

    for i in range(e):
        a, b = map(int, input().split())
        board[a][b] = 1

    s, g = map(int, input().split())  # 경로의 존재를 확인할 출발 s 도착 g

    v = s
    visited[v] = True

    while True:
        for w in range(v + 1):
            if board[v][w] == 1 and not visited[w]:
                stack.append(v)
                v = w
                visited[w] = True
                break
        else:
            if stack:  # stack이 true라면 즉, 비어있지 않다면
                v = stack.pop()  # 되돌아갈일만 남음..
            else:  # 비어있다면
                break  # 갈 곳이 없음

    if visited[g] == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
