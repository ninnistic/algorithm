def back_tracking(a, k, total):
    global min_sum

    if a == k:
        if total < min_sum:
            min_sum = total
    elif total > min_sum:
        return

    else:
        for j in range(n):
            if not visited[j]:
                visited[j] = True
                back_tracking(a+1, k, total+graph[a][j])
                visited[j] = False



t = int(input())
for tc in range(1, t+1):
    n = int(input())
    graph = []
    visited = [False]*n
    min_sum = 100

    for _ in range(n):
        nums = list(map(int, input().split()))
        graph.append(nums)

    # n = 배열의 길이
    back_tracking(0,n,0)
    print(f"#{tc} {min_sum}")