# 큰 사각형 - 작은 사각형
# 작은 사각형은 큰 사각형의 세로 가로랑 인접하지 않음
# 작은 사각형의 가로값은 큰 사각형 세로값 전에 오는 가로갓 - 큰 사각형 세로값 담에 오는 가로값
# 작은 사각형의 세로값은 큰 사각형 가로값 전에 오는 세로값 - 큰 사각형 가로값 담에 오는 세로값
melon = int(input()) # 참외의 개수

width = []
height = []
order = []
# 육각형 이라고 했으므로 6
for i in range(6):
    #방향 #길이
    direction, length = map(int, input().split())
    if direction == 1 or direction == 2:
        width.append(length)
        order.append(length)
    else:
        height.append(length)
        order.append(length)
# print(width, height)
big_farm = max(width) * max(height)

# max 가로 인덱스 구하기, max 세로 인덱스 구하기
w_idx = order.index(max(width))
h_idx = order.index(max(height))

# 인덱스 에러 처리 위해서 mod 6 -> 이건 블로그 도움 받음...
small_width = abs(order[(w_idx-1) % 6] - order[(w_idx+1) % 6])
small_height = abs(order[(h_idx-1) % 6 ] - order[(h_idx+1) % 6])

res = (big_farm - (small_width * small_height)) * melon
print(res)



