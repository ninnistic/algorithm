T = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())
    # 2차원 배열 값은 보통 graph라고 명칭
    graph = [[0] * (V+1) for _ in range(V+1)]

    visited = [False] * (V+1)
    stack = []

    for i in range(E):
        a, b = map(int, input().split())  # 노드에 연결된 페어가 E개씩 있음
        graph[a][b] = 1  # 두 점이 이어졌다는 뜻

    # 2차원 배열 목록 다 불러오고
    S, G = map(int, input().split())

    v = S  # 시작점
    visited[v] = True

    while True:
        for w in range(V+1):
            # v 출발점에서 W 도착점까지갈 수 있다면?
            # ex) 만약 a,b가 연결 되어있고 아직 b에 방문한 적이 없다면
            # v = 시작점 w = 도착점
            if graph[v][w] == 1 and not visited[w]:
                stack.append(v)
                v = w
                visited[w] = True  # 방문함
                break
        else:
            if stack:
                v = stack.pop()
            else:  # 스택이 비어있다면?
                break  # 갈 곳이 없다는 뜻이므로, 전체 while문을 끝냄

    if visited[G] == True:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
