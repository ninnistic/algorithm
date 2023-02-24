def combinations(res):
    if len(res) == 6:
        print(*res)
        return
    if k == 0:
        return
    else:
        for i in nums:
            if i not in res:
                res.append(i)
                combinations(res)
                res.pop()


k, *nums = map(int, input().split())
# 이러면 k랑 nums를 각각 받기 가넝
result = []
combinations(result)
