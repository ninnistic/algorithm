# 문어박사님의 달팽이 숫자의 강의를 보고 배웠읍니다...
# 대기번호 k에게 배정될 좌석번호 x,y를 구하기
# counts를 활용...
# 배정할 수 없다면 0 출력

c, r = map(int, input().split())
k = int(input()) # 관객 번호
a = b = 1 # 구할 좌표 1으로 초기화
# 좌석 만들어주기
seats = [[0] * r for _ in range(c)]

delta = [(0,1), (1, 0), (0, -1), (-1,0)]

seats[0][0] = 1
i = j = 0 # j = 행, i = 열
counts = 1 # 대기번호 count
cycle = 0

seats[i][j] = counts # 시작값에 대기번호 넣고
counts += 1 # counts 1 증가


while counts <= c * r:
    # cycle은 0인상태
    ni, nj = i+delta[cycle][0], j+delta[cycle][1]
    if 0 <= ni < c and 0<= nj < r and seats[ni][nj] == 0:
        i, j = ni, nj
        seats[i][j] = counts
        if k == counts:
            a = i + 1
            b = j + 1
            break
        else:
            counts += 1
    else:
        cycle = (cycle+1) % 4

if k > c * r :
    print(0)
else:
    print(a, b)







