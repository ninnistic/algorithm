# 노수혁님 코드 (SWEA 1979 sol-1)
loop = int(input())

for case in range(1, loop+1):
    N, M = map(int, input().split())
    board = [input().split() for _ in range(N)]
    cnt_vtc, cnt_wth = [0] * N, [0] * N
    cnt = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] != '0':
                cnt_wth[i] += 1
                cnt_vtc[j] += 1
            else:
                if cnt_wth[i] == M:
                    cnt += 1
                if cnt_vtc[j] == M:
                    cnt += 1
                cnt_wth[i] = 0
                cnt_vtc[j] = 0
        if cnt_wth[i] == M:
            cnt += 1

    cnt += cnt_vtc.count(M)

    print('#{} {}'.format(case, cnt))
