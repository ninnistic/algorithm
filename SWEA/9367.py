# 어차피 구간의 길이가 1임!!!

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    carrots = list(map(int, input().split()))

    sequence = 1  # 연속하지 않을경우의 초기값은 1
    total = 1       # 결과도 마찬가지로 초기값은 1

    for i in range(1, n):
        # ex) carrot[1] 의 값이 carrot[0]보다 크다면 (연속) (앞보다 뒤가 크다면)
        if carrots[i] > carrots[i-1]:
            sequence += 1       # 어차피 구간의 최소길이는 1이기 때문에 sequence에 +1을 해준다
        else:
            sequence = 1     # 그게 아니고, 연속이 아니라면 sequence는 그대로 1로 한다.
        if total < sequence:   # 만약에 total과 비교해서 sequence가 크다면
            # total은 sequence로 재할당 해준다. (그래서 45로 연속이 되더라도 123의 3번연속이 다시)
            total = sequence

    print(f"#{tc} {total}")
