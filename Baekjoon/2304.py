n = int(input()) # 기둥의 개수

cols = [list(map(int, input().split())) for _ in range(n)]

# [[2, 4], [11, 4], [15, 8], [4, 6], [5, 3], [8, 10], [13, 6]]
side = []
top = []

# 양 옆 side 길이 먼저 추가
side.append(cols[0][1])
side.append(cols[-1][1])

# 가장 높은 기둥 좌표 구하기
for x, y in cols:
