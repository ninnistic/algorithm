

t = int(input())

for tc in range(1, t+1):
    n = int(input())  # 노선의 수

    stops = [0] * 1001  # 정류장의 번호 1번부터 1000번까지 + 0번 포함

    for i in range(n):
        bus, start, end = map(int, input().split())  # 버스 종류, 출발점, 도착점

        stops[start] += 1       # 시작점, 도착점은 언제나 버스가 정차하므로
        stops[end] += 1

        if bus == 1:                           # 만약 버스가 일반이라면
            for a in range(start+1, end):
                # start(는 이미 추가되었음) start +1 부터 end(-1)까지 1씩 증가
                stops[a] += 1

        if bus == 2:                            # 만약 버스가 급행이라면
            for b in range(start+1, end):           # 급행버스가 출발점에서 종점까지 가는 동안
                if start % 2 == 0 and b % 2 == 0:             # 만약 출발지가 짝수번호고, 정류장이 짝수번호라면
                    stops[b] += 1                               # 짝수 정류장마다 +1
                elif start % 2 == 1 and b % 2 == 1:             # 홀수도 마찬가지
                    stops[b] += 1

        if bus == 3:                           # 만약 광역 버스라면
            for c in range(start+1, end):           # 광역버스가 출발점에서 종점까지 가는동안
                if start % 2 == 0 and c % 4 == 0:      # 출발지가 짝수이고, 4의 배수 정류장이라면
                    stops[c] += 1                          # 4의 배수 정류장 += 1
                elif start % 2 == 1 and c % 3 == 0 and not c % 10 == 0:    # 출발지가 홀수, 3의 배수, 10의 배수 정류장이 아님
                    stops[c] += 1  # ++;

    print(f"#{tc} {max(stops)}")
