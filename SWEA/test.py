n = int(input())
dice = [list(map(int, input().split())) for _ in range(n)]
max_sum = []  # 0~5 인덱스 시작을 기준으로 주사위의 옆면 최고치 합을 모아 놓을 리스트 선언
# 주사위 하나의 길이 만큼 돈다.
for i in range(6):
    start = i
    result = 0
    # 입력받은 주사위의 길이만큼 돌기.
    for j in range(len(dice)):

        # 만약 주사위의 인덱스가 0 이나 5라면
        if start == 0 or start == 5:
            # 0, 5번을 제외한 나머지 주사위 면중 가장 큰 값을 더하기
            result += max(dice[j][1:5])
            # 만약 인덱스가 마지막이 아니고 0이면
            if j != len(dice) - 1 and start == 0:
                start = dice[j + 1].index(dice[j][5])
            elif j != len(dice) - 1 and start == 5:
                start = dice[j + 1].index(dice[j][0])
        # 만약 주사위의 인덱스가 2 이나 4라면
        elif start == 2 or start == 4:
            # 2, 4번을 제외한 나머지 주사위 면중 가장 큰 값을 더하기
            result += max(dice[j][0:2] + [dice[j][3]] + [dice[j][5]])
            if j != len(dice) - 1 and start == 2:
                start = dice[j + 1].index(dice[j][4])
            elif j != len(dice) - 1 and start == 4:
                start = dice[j + 1].index(dice[j][2])

        # 만약 주사위의 인덱스가 1 이나 3라면
        elif start == 1 or start == 3:
            result += max([dice[j][0]] + [dice[j][2]] + dice[j][4:])
            if j != len(dice) - 1 and start == 1:
                start = dice[j + 1].index(dice[j][3])
            elif j != len(dice) - 1 and start == 3:
                start = dice[j + 1].index(dice[j][1])

    # N개의 주사위를 다 돈 N개의 옆면 합을 대입
    max_sum.append(result)

print(max(max_sum))