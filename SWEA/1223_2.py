for tc in range(1, 11):
    n = int(input())
    code = input()  # 길이
    stack = []
    nums = []

    for i in code:
        if i.isdigit():
            nums.append(i)
        else:
            if i == '+':
                if len(stack) == 0:
                    stack.append(i)
                elif stack[-1] == '+':
                    nums.append(i)
                else:
                    while True:
                        if len(stack) == 0:
                            stack.append(i)
                            break
                        else:
                            nums.append(stack.pop())
            else:
                if len(stack) == 0:
                    stack.append(i)
                elif stack[-1] == '*':
                    nums.append(i)
                else:
                    stack.append(i)
    for i in range(len(stack)):
        nums.append(stack.pop())


    for i in nums:
        if i.isdigit():
            stack.append(i)
        else:
            second = int(stack.pop())
            first = int(stack.pop())
            if i == '+':
                res = first + second
                stack.append(res)
            else:
                res = first * second
                stack.append(res)
    print(f"#{tc} {stack[0]}")
