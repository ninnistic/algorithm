def bfs(start):
    q = []
    q.append(start)
    visited1[start] = 1
    while q:
        start = q.pop()
        print(start, end = " ")
        for i in range(1, n+1):
            if visited1[i] == 0 and graph[start][i] == 1:
                q.append(i)
                visited1[i] = 1


def dfs(start):
    visited1[start] = 1
    print(start, end = " ")
    for i in range(1, n+1):
        if not visited2[i] and graph[start][i] == 1:
            dfs(i)


n, m, v = map(int, input().split())
# 정점의 개수 # 간선의 개수 # 정점의 번호
graph = [[0] * (n+1) for _ in range(n+1)]
visited1 = [0] * (n+1)
visited2 = [False] * (n+1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

dfs(v)
print()
bfs(v)
