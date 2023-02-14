n = int(input())
room = [list(input()) for _ in range(n)]  # 가로방

across = 0
down = 0
counts = 0

for i in range(n):  # n x n 크기의 방
    for j in range(n):
        if room[i][j] == 'X':
            counts = 0
        elif room[i][j] == '.':
            counts += 1
            if counts == 2:
                across += 1
    counts = 0

for i in range(n):
    for j in range(n):
        if room[j][i] == 'X':
            counts = 0
        elif room[j][i] == '.':
            counts += 1
            if counts == 2:
                down += 1
    counts = 0

print(across, down)
