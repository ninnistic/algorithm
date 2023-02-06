import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input()) #당근의 개수
    C_lst = list(map(int,input().split())) # 당근 사이즈

    cnt_res = 1 # 최댓값 저장할 변수
    cnt = 1 # 연속하는 경우가 생길때마다 기록할 변수
    for n in range(N-1):
        if C_lst[n] + 1 == C_lst[n + 1]: # 1을 더한값이 뒤의 값과 같으면
            cnt += 1 # 횟수를 하나 증가시키고
            if cnt_res <= cnt: # 최댓값보다 크면
                cnt_res = cnt # 최댓값을 바꾼다.
        else: # 아니라면
            cnt = 1 # cnt 원상복구
    print(f'#{tc} {cnt_res}')