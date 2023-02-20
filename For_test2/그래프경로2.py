t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split())
    board = [[0] * (V+1) for _ in range(V+1)]

    visited = [False]*(V+1)
    stack = []

    for i in range(E):
        a, b = map(int, input().split())
        board[a][b] = 1

    s, g = map(int, input().split())

    v = s
    visited[v] = True

    while True:
        for w in range(V+1):
            if board[v][w] == 1 and not visited[w]:
                stack.append(v)
                v = w
                visited[w] = True
                break
        else:
            if stack:
                v = stack.pop()
            else:
                break

    if visited[g] == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")