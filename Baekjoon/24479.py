# N개의 정점과 M개의 간선, '무방향' 그래프
# 정점번호 : 1번부터 N번
# 간선의 가중치 == 1(?)
# 정점 : R에서부터, 노드의 방문순서 출력하기~!
# N : 정점의 수, M : 간선의 수, R : 시작 정점
# M 개의 줄 => 간선정보 u, v
# 정점 u와 v의 가중치 1인 양방향 간선...(가중치가 뭔솔..?)


n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n+1)
stack = []
res = [0] * (n+1)
counts = 1

start = r
visited[start] = True
res[start] = counts

while True:
    for end in graph[start]:
        if not visited[end]:
            stack.append(start)
            start = end
            visited[end] = True
            counts += 1
            res[start] = counts
            break
    else:
        if stack:
            start = stack.pop()
        else:
            break




