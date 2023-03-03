n, m = map(int, input().split()) # n = 카드장수 , m = 만들어야 하는 수
num_list = list(map(int, input().split()))

answer = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            total = num_list[i] + num_list[j] + num_list[k]

            if total <= m and total > answer:
                answer = total

print(answer)