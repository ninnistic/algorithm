


t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    arr_t = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr_t[i][j] = arr[j][i]
    ans = "NO"

    #가로
    for i in range(n):
        for j in range(n-4):
            if arr[i][j] == arr[i][j+1] == arr[i][j+2] == arr[i][j+3] == arr[i][j+4] == 'o':
                ans = "YES"
                break
    #세로
    for i in range(n):
        for j in range(n-4):
            if arr_t[i][j] == arr_t[i][j+1] == arr_t[i][j+2] == arr_t[i][j+3] == arr_t[i][j+4]== 'o':
                ans = "YES"
                break

    #대각선
    for i in range(n-4):
        for j in range(n-4):
            if arr[i][j] == arr[i+1][j+1] == arr[i+2][j+2] == arr[i+3][j+3] == arr[i+4][j+4]== 'o':
                ans = "YES"
                break

    #반대 대각선
    for i in range(n-4):
        for j in range(n-1, -1, -1):
            if arr[i][j] == arr[i+1][j-1] == arr[i+2][j-2] == arr[i+3][j-3] == arr[i+4][j-4]== 'o':
                ans = "YES"
                break

    print(f"#{tc} {ans}")





