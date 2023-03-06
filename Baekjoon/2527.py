for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int(input().split()))
    # 2네모 2점의 x선상과 1네모 1점의 x선상이 같고 2네모 y가 1네모 y보다 크고..
    # 각각의 경우 4방 반복
    if p2 == x1 and q2 > y1 and q1 > y2:
        print('b')
        continue
    if q2 == y1 and p1 > x2 and p2 > x1:
        print('b')
        continue
    if x2 == p1 and q2 > y1 and q1 > y2:
        print('b')
        continue
    if y2 == q1 and p1 > x2 and p2 > x1:
        print('b')
        continue
    # 같은 점
    # 서로 모서리가 닿아 있을 때
    if [x1, y1] == [p2, q2] or [p1, y1] == [x2, q2] or [x1, q1] == [p2, y2] or [p1, q1] == [x2, y2]:
        print('c')
        continue
    # 2네모 1점 > 1네모 2점
    # 1네모 1점 > 2네모 2점
    # 겹치지 않음
    if x2 > p1 or x1 > p2 or y2 > q1 or y1 > q2:
        print('d')
        continue

    # 다 아니면 직사각형
    print('a')

