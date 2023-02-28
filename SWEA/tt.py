t = int(input())
dice = [list(map(int, input().split())) for _ in range(t)]
max_sum = [] # 최고 합 놓기

for i in range(6): # 주사위 하나 만큼 돌면서
    eye = i
    res = 0
    for j in range(len(dice)): #입력받은 주사위 길이만큼
        if eye == 0 or eye == 5:
            res += max(dice[j][1:5])
            if j != len(dice)-1 and eye == 0:
                eye = dice[j+1].index(dice[j][5])
            if j != len(dice)-1 and eye == 5:
                eye = dice[j+1].index(dice[j][0])
        if eye == 1 or eye == 4:
            res += max(dice[j][1:5])
            if j != len(dice)-1 and eye == 0:
                eye = dice[j+1].index(dice[j][5])
            if j != len(dice)-1 and eye == 5:
                eye = dice[j+1].index(dice[j][0])
        if eye == 2 or eye == 3:
            res += max(dice[j][1:5])
            if j != len(dice)-1 and eye == 0:
                eye = dice[j+1].index(dice[j][5])
            if j != len(dice)-1 and eye == 5:
                eye = dice[j+1].index(dice[j][0])