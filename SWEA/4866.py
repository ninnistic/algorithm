t = int(input())

for tc in range(1, t+1):
    stack = []
    line = input()
    result = 1

    # 입력 받은 문자열을 도는동안
    for i in line:
        # 왼쪽 괄호라면 스택에 넣는다
        if i == '{' or i == '(':
            stack.append(i)

        # i 가 '}' 일 때
        elif i == '}':
            # stack의 길이가 0이거나, stack에서 pop한 값이 '{'이 아니라면
            if len(stack) == 0:
                result = 0
                break
            elif stack.pop() != '{':
                result = 0
                break

        # i가 ')'인데
        elif i == ')':
            # stack의 길이가 0이거나, stack에서 pop한 값이 '('이 아니라면
            if len(stack) == 0:
                result = 0
                break
            elif stack.pop() != '(':
                result = 0
                break
    # stack에 값이 남아 있다는 건 안정적인 문자열이 아님
    if len(stack) > 0:
        result = 0

    print(f"#{tc} {result}")
