
t = int(input())

for tc in range(1, t+1):
    n = int(input())
    board = [input().split() for _ in range(n)]
    arr1 = [[0]*n for _ in range(n)]
    arr2 = [[0]*n for _ in range(n)]
    arr3 = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr1[i][j] = board[n-1-j][i]
            arr2[i][j] = board[n-1-i][n-1-j]
            arr3[i][j] = board[j][n-1-i]
    print(f"#{tc}")
    for a, b, c in zip(arr1, arr2, arr3):
        print(f"{''.join(a)} {''.join(b)} {''.join(c)}")

# 준형이가 알려준 방법
# 패턴이 있음 .
# -> - > -> 이렇게 가는건 쉽기 때문에 이런 방식으로 풀어보아라.
