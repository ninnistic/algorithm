# 무방향 그래프 -> 서로 이어져 있음
# n = 정점의 수 , m = 간선의 수, r = 시작 정점
# u, v (간선정보)
# 시작정점에서 방문할 수 없는 경우라면 0
# 가중치??
n, m, r = map(int, input().split())
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)

# 인접리스트에 값을 넣기
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)


def dfs(v, e, r):  # v: 정점 e: 간선 r: 시작
