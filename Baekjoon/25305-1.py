N, k = map(int, input().split())
scores = list(map(int, input().split()))


for i in range(N - 1, 0, -1):
    for j in range(i):
        if scores[j] > scores[j + 1]:
            scores[j], scores[j + 1] = scores[j + 1], scores[j]

print(scores[-k])
