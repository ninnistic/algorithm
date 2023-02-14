t = int(input())

for tc in range(1, t+1):

    # 입력 받은 문자열
    line = list(input())

    i = 0
    while i < len(line)-1:
        if line[i] == line[i+1]:
            line.pop(i)
            line.pop(i)
            i = 0
        else:
            i += 1

    print(f"#{tc} {len(line)}")
