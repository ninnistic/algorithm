t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr = [input().split() for _ in range(n)]
    a1 = [[0]*n for _ in range(n)]
    a2 = [[0]*n for _ in range(n)]
    a3 = [[0]*n for _ in range(n)]

    # 회전 각도에 따른 위치 값을 저장
    for i in range(n):
        for j in range(n):
            a1[i][j] = arr[n-1-j][i]
            a2[i][j] = arr[n-1-i][n-1-j]
            a3[i][j] = arr[j][n-1-i]

    print(f"{test_case}")
    for a, b, c in zip(a1, a2, a3):
        print(f"{''.join(a)} {''.join(b)} {''.join(c)}")
