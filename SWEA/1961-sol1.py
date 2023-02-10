t = int(input())
for test_case in range(1, t+1):
    n = int(input())
    arr_t = list(map(list, zip(*arr)))  # 세로
    arr = [input().split() for _ in range(n)]
    a1 = [[0]*n for _ in range(n)]
    a2 = [[0]*n for _ in range(n)]
    a3 = [[0]*n for _ in range(n)]

    # 전치 배열과 읽는 방향에 따른 처리
    print(f"{test_case}")
    for i in range(n):
        print(
            f"{''.join(arr_t[i][::-1])} {''.join(arr[n-1-i][::-1])} {''.join(arr_t[n-1-i])}")
