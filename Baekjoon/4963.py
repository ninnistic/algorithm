
# 섬의 개수
# 1을 기준으로 8방 델타탐색 => 1이 있다? 0 으로 바꿔줌
import sys
input = sys.stdin.readline
def travel(x, y):
    q = [(x, y)]
    world[x][y] = 0 # 방문한 곳 0 처리
    delta = [(0,1), (1, -1), (1, 0), (1, 1), (0, -1), (-1,-1), (-1,0), (-1,1)]

    while q:
        x, y = q.pop(0)
        for k in delta:
            nx = x + k[0]
            ny = y + k[1]
            if 0 <= nx < h and 0 <= ny <w and world[nx][ny] == 1:
                world[ny][ny] = 0
                q.append((nx, ny))



while True:
    w, h = map(int, input().split()) # w = 너비, h = 높이
    if w == 0 and h == 0:
        break

    world = [list(map(int, input().split())) for _ in range(h)]
    counts = 0

    for i in range(h):
        for j in range(w):
            if world[i][j] == 1:
                travel(i, j)
                counts += 1

    print(counts)