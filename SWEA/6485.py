t = int(input())
for tc in range(1, t+1):
    n = int(input())

    # counts = 버스정류장 배열의 길이ㄴ
    counts = [0] * 5001

    # n개동안 a , b의 입력값을 받아준다
    for i in range(n):
        a, b = map(int, input().split())
        # a부터 b까지 지나가며 counts를 세어준다.
        # 여기서 j는 지나가는 버스 정류장의 index와 동일
        for j in range(a, b+1):
            counts[j] += 1
    # p를 입력받고
    p = int(input())
    # 결과를 넣을 list 하나 생성
    result = []
    for i in range(p):
        # route는 정류장 번호를 부르는 값이다.
        route = int(input())
        # counts 1번 idx에 1번 정류장의 노선 개수가 들어있으므로
        # 가져와서 append 해준다.
        result.append(counts[route])

    print(f'#{tc}', *result)
