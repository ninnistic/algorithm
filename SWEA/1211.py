# 99 가 되면 종료!
# 아래로 진행할땐 좌 우만 체크하기
# 좌 우로 진행할땐 아래로만 내려가면 된다

t = 10
for test_case in range(1, t+1):
    _ = int(input())
    arr = [[0] + list(map(int, input().split()))]
    mn = 100*100  # 최솟값
    for sj in range(1, 101):
        si, cnt, dj = 0, 0, 0  # si = 시작하는 i / dj = 움직이는 j
        # [1] : 시작지점 찾기
        if arr[si][sj] != 1:
            continue

        ci, cj = si, sj

        while ci < 99:  # current i
            cnt += 1
            if dj == 0:  # 방향이 0이라면
                if arr[ci][cj-1] == 1:  # 좌측
                    dj -= 1
                    cj -= 1
                elif arr[ci][cj+1] == 1:  # 우측
                    dj = 1
                    cj += 1
                else:
                    ci += 1
            else:
                if arr[ci][cj+dj] == 1:
                    cj += dj
                else:  # 진행방향이 막힌경우에는 아래로
                    dj = 0
                    ci += 1
        if mn >= cnt:
            mn, ans = cnt, sj-1

    print(f'#{test_case} {ans}')
