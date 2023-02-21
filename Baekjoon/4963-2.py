import sys
input = sys.stdin.readline
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break

    world = [list(map(int, input().split())) for _ in range(h)]
    counts = 0

    for i in range(h):
        for j in range(w):
            if world[i][j] == 1:
                counts += 1
                q = [(i, j)]
                world[i][j] = 0

                delta = [(0, 1), (1, -1), (1, 0), (1, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]

                while q:
                    x, y = q.pop(0)
                    for k in delta:
                        nx = x + k[0]
                        ny = y + k[1]
                        if 0 <= nx < h and 0 <= ny < w and world[nx][ny] == 1:
                            world[nx][ny] = 0
                            q.append((nx, ny))
    print(counts)
