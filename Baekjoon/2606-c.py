# 1번과 연결 되어 있는 컴퓨터들은 바이러스에 걸림 -> 즉 1번을 시작점으로
# 1번과 연결된 곳을 모두 찾는다.
# input : 1) 컴퓨터의수
#         2) 간선의 수
#         3) 컴퓨터의 번호 쌍

pc = int(input())  # 컴퓨터의 수
e = int(input())  # 간선의 수

graph = [[0] * (pc+1) for _ in range(pc+1)]

for _ in range(e):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (pc+1)
stack = []
res = []  # 1번을 통해 바이러스에 걸리게되는 컴퓨터 수를 세기 위함

v = 1  # 시작점은 1번으로 고정
visited[v] = True
# 여기서 res.append(v) 하지 않음 1번은 포함하지 않을 것이므로

while True:
    for w in range(pc+1):
        if graph[v][w] == 1 and visited[w] == False:
            stack.append(v)
            v = w
            visited[w] = True
            res.append(w)
            break
    else:
        if stack:
            v = stack.pop()
        else:
            break

print(len(res))
