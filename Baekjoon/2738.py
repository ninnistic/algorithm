n, m = map(int, input().split())
# n개의 줄에 원소 m 개
matrix_a = [list(map(int, input().split())) for _ in range(n)]
matrix_b = [list(map(int, input().split())) for _ in range(n)]
res = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        res[i][j] = matrix_a[i][j] + matrix_b[i][j]

for i in range(n):
    print(*res[i])