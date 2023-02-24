
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    a = n // 10
    paper = [0] * (a+1)
    paper[0] = 0
    paper[1] = 1
    paper[2] = 3
    for i in range(3, a+1):
        paper[i] = paper[i-1] + paper[i-2] * 2
    print(f"#{tc} {paper[-1]}")