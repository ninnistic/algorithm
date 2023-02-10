def counts(arr):
    ans = 0
    for lst in arr:
        cnt = 0
        # 리스트의 숫자를 하나씩 꺼내기
        for n in lst:
            if n == 1:  # 단어를 넣을 수 있는 공백
                cnt += 1
            else:               # 막힘
                if cnt == k:
                    ans += 1
                cnt = 0  # 카운트 초기화


t = int(input())
for test_case in range(1, t+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) + [0]
           for _ in range(n)] + [[0]*(n+1)]

    # 튜플이므로 리스트에 넣어준다. map을 이용해서
    arr_t = list(map(list, (zip(*arr))))
    ans = counts(arr) + counts(arr_t)
