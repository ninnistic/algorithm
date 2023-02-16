# t = int(input())

n = int(input())
board = [list(input()) for _ in range(n)]
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


visited = [False] * (n+1)
stack = []

starts = []
for i in range(n):
    for j in range(n):
        if board[i][j] == '2':
            start = 

        