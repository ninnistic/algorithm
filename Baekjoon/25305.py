# n명중 점수가 가장 높은 k명은 상을 받는다
# 커트라인 == 가장 낮은 점수
# sort를 쓰지 않고 풀어야함!
# bubble sort를 사용해보자..! -> 그 이후에 k명 만큼 값을 구하고, 최솟값을 찾자

n, k = map(int, input().split())
scores = list(map(int, input().split()))

for i in range(n-1):
    tmp = 0
    for j in range(n-1):
        if scores[j] > scores[j+1]:
            tmp = scores[j]
            scores[j] = scores[j+1]
            scores[j+1] = tmp

print(scores[-k])
