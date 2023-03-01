
n = int(input())  # 스위치 개수
switches = [0] + list(map(int, input().split())) # 각 스위치
m = int(input()) # 학생 수
students = [list(map(int, input().split())) for _ in range(m)] # 성별, 받은 번호
# [[1, 3], [2, 3]]

for x, y in students:
    if x == 1:
        for i in range(y, n+1, y):
            switches[i] = 1 - switches[i]
    else :
        switches[y] = 1 - switches[y]
        for k in range(n // 2):
            # 범위 초과하거나 범위 미만이 아니도록
            if y + k > n or y - k < 1 :
                break
            if switches[y+k] == switches[y-k]:
                switches[y+k] = 1 - switches[y+k]
                switches[y-k] = 1 - switches[y-k]
            else:
                break

for i in range(1, n+1):
    print(switches[i], end=' ')
    if i % 20 == 0:
        print( )