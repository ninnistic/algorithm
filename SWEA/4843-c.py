def sort_nums(nums, n):
    # 선택 정렬 사용하기
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if nums[min_idx] > nums[j]:
                min_idx = j
        nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums


t = int(input())

for tc in range(1, t+1):
    n = int(input())
    nums = list(map(int, input().split()))
    sort_nums(nums, n)  # 정렬된 nums가 return
    result = []

    while len(nums) != 0:
        result.append(nums.pop(-1))
        result.append(nums.pop(0))

    print(f"#{tc}", *result[:10])
