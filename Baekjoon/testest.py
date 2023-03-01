t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split()) # n개의 과목 중에 k개의 과목 선택 가능
    scores = list(map(int, input().split())) # n개 과목에 대한 점수
    scores.sort(reverse=True)
    print(f"#{tc} {sum(scores[:k])}")