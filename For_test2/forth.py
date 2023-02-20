t = int(input())

for tc in range(1, t+1):
    code = input().split()
    stack = []
    res = 0

    for i in code:
        if i == '.':
            break

        elif i.isdigit():
            stack.append(int(i))

        else : # i가 연산자라면
            if len(stack) < 2:
                stack.append('error')
                stack.append('error')
                break
            else : # 연산자일때 stack의 길이가 2개보다 적다면? stack 비워주고 break
                second = int(stack.pop())
                first = int(stack.pop())
                if i == '+':
                    stack.append(first + second)
                elif i == '-':
                    stack.append(first - second)
                elif i == '*':
                    stack.append(first * second)
                elif i == '/':
                    stack.append(first // second)

    if len(stack) > 1:
        res = 'error'
    else:
        res = stack.pop()

    print(f"#{tc} {res}")

