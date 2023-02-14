# a -> b로 가는 길이 존재하는지 조사 == 연결되었다
# 일방통행 == 단방향(무방향이 아님)
# 0에서 99로 고정 (총 100개 )
# 뒤로 거슬러 올라가는 것은 안됨
# input : 1) tc번호 , 길의 총 개수
#         2) 순서 쌍
# output : a - b == 1인지 확인하라

for _ in range(10):  # tc 10개
    tc, total = map(int, input().split())
    arr = list(map(int, input().split()))
    graph = [[0] * 100 for _ in range(100)]

    for i in range(total):
        a = arr[2*i]
        b = arr[2*i+1]
        graph[a][b] = 1  # 단방향

    visited = [False] * 100

    v = 0
    visited[v] = True
    stack = []

    while True:
        for w in range(100):
            if graph[v][w] == 1 and visited[w] == False:
                stack.append(v)
                v = w
                visited[w] = True
                break

        else:
            if stack:
                v = stack.pop()
            else:
                break

    if visited[99]:
        print(f"#{tc} 1")
    else:
        print(f"#{tc} 0")
