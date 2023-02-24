for tc in range(1, 11):
    length, nums = input().split()
    stack = []

    for i in nums:
        if stack: # stack이 비어있지 않으면
            if stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)
        else:
            stack.append(i)

    result = ''.join(stack)
    print(f"#{tc} {result}")
