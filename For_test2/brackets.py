t = int(input())

for tc in range(1, t+1):
    code = input()
    stack = []
    result = 1

    for i in code:
        if i == '(' or i == '{':
            stack.append(i)

        if i == ')':
            if len(stack) == 0:
                result = 0
                break
            elif stack.pop() != '(':
                result = 0
                break

        if i == '}':
            if len(stack) == 0:
                result = 0
                break
            elif stack.pop() != '{':
                result = 0
                break

    if len(stack) > 0:
        result = 0

    print(f"#{tc} {result}")
