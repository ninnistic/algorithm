t = int(input())
for tc in range(1, t+1):
    n = int(input())
    ones = [1] * (n+2)
    board = [1] + [[0] * n for _ in range(n)] + [1]
    new_list = ones + board + ones
    print(board)
