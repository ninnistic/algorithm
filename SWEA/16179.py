t = int(input())

for tc in range(1, t+1):
    # k = 버스가 이동할 수 있는 최대거리, n = 종점의 위치, m = 정류장 개수
    k, n, m = map(int, input().split())

    chargers = list(map(int, input().split()))  # 정류장 번호 정보 # [1,3,5,7,9]
    stops = [0] * (n+1)  # 0번부터 n번까지 # [0] -> [10]

    # [0,1,0,1,0,1,0,1,0,1,0]
    for bus in range(n):
        for charger in range(m):
            stops[chargers[charger]] = 1

    for i in range(n-m+1):
        counts = 0
        for j in chargers:
            if i + k >= j:
                counts += 1
                i += k
            else:
                counts = 0

    print(f"#{tc} {counts}")
