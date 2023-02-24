# 트리의 부모 찾기
# 행렬로 풀면 메모리 초과가 난대서.... 인접행렬로 도오전

n = int(input())

# 0부터 7까지의 정보를 담기 위해 n+1해줌
graph = [[] for _ in range(n+1)]

# n-1줄
for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n+1)
stack = []
parents = [0] * (n+1)

# 시작점은 1번
v = 1
visited[v] = True

while True:
    for w in graph[v]:
        if visited[w] == False:
            stack.append(v)
            parents[w] = v
            v = w
            visited[w] = True
            break

    if stack:
        v = stack.pop()
    else:
        break

print(*parents)
