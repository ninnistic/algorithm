'''
10 5 # 가로 세로
3 # 상점의 개수
1 4 # 방향, 거리
3 2 # 방향, 거리
2 8
2 3 # 동근이의 방향, 거리
'''

# 가로 세로
width, height = map(int, input().split())
n = int(input()) # 상점의 개수
loc = int(input())
stores = [list(map(int, input().split())) for _ in range(loc+1)] # 상점 정보
dg = stores.pop() #동근은 맨 마지막에
res = 0

# 동근이가 북쪽에 있으면
if dg[0] == 1 :
    for di, dis in stores:
        if di == 1: # 상점이 북쪽일 때
            res += abs(dg[1] - dis) # 동근거리 - 상점거리
        if di == 2: # 상점이 남쪽일 때
            left_dis = dg[1] + height + dis # 동근거리 + 높이 + 거리
            right_dis = width - dg[1] + height + width - dis
            res += min(left_dis, right_dis)
        if di == 3: # 서쪽
            res += dg[1] + dis
        if di == 4: # 동쪽
            res += width - dg[1] + dis

if dg[0] == 2 :
    for di, dis in stores:
        if di == 1:
            left_dis = dg[1] + height + dis
            right_dis = width - dg[1] + height + width - dis
            res += min(left_dis, right_dis )
        if di == 2:
            res += abs(dg[1] - dis)
        if di == 3:
            res += dg[1] + height - dis
        if di == 4:
            res += width - dg[1] + height - dis

if dg[0] == 3 :
    for di, dis in stores:
        if di == 1:
            res += dg[1] + dis
        if di == 2:
            res += height - dg[1] + dis
        if di == 3:
            res += abs(dg[1] - dis)
        if di == 4:
            left_dis = dg[1] + height + dis
            right_dis = height - dg[1] + width + height - dis
            res += min(left_dis, right_dis)


if dg[0] == 4 :
    for di, dis in stores:
        if di == 1:
            res += dg[1] + width - dis
        if di == 2:
            res += height - dg[1] + width - dis
        if di == 3:
            left_dis = height - dg[1] + width + height - dis
            right_dis = dg[1] + width + dis
            res += min(left_dis, right_dis)
        if di == 4:
            res += abs(dg[1] - dis)

print(res)
