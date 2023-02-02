count = 0
for i in range(8):
    chess = list(input())
    if i % 2 == 0:  # 짝수줄이라면
        for j in range(len(chess)):
            if j % 2 == 0:  # j도 짝수칸이라면
                if chess[j] == 'F':
                    count += 1
    else:                       # 그게 아니고 j가 홀수줄이고
        for j in range(len(chess)):
            if j % 2 == 1:  # j가 홀수칸이라면
                if chess[j] == 'F':  # 홀수칸의 글자가 F라면
                    count += 1

print(count)
