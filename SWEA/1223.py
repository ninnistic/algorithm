
for tc in range(1, 11):
    n = int(input())
    code = input()  # 길이
    stack = []
    nums = []
    for i in code:
        if i.isdigit():
            nums.append(int(i))
        else:
            if stack:
                if i == '+' and stack[-1] =='+':
                    stack.append(i)
                elif i == '+' and stack[-1] == '*':
                    stack.pop()
                    second = nums.pop()
                    first = nums.pop()
                    nums.append(first * second)
                    stack.append(i)
                elif i == '*' and stack[-1] == '+':
                    stack.append(i)
                elif i == '*' and stack[-1] == '*':
                    stack.pop()
                    second = nums.pop()
                    first = nums.pop()
                    nums.append(first * second)
                    stack.append(i)
            else:
                stack.append(i)

    else:
        if len(nums) >= 2 and stack:
            for _ in range(len(stack)):
                if stack[-1] == '+':
                    stack.pop()
                    second = nums.pop()
                    first = nums.pop()
                    stack.append(first + second)

                else:
                    stack.pop()
                    second = nums.pop()
                    first = nums.pop()
                    stack.append(first * second)
            print(f"#{tc} {nums.pop()}")
        elif len(nums) == 1:
            print(f"#{tc} {nums.pop()}")
