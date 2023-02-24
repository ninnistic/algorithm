t = int(input())
for tc in range(1, t+1):
    line = input()
    stack = []

    for i in line:
        if not stack: # 스택이 비어있다면
            stack.append(i)
        elif stack[-1] != i: # 스택의 탑과 i가 다르다면 stack에 넣는다.
            stack.append(i)
        else: # 스택이 비어있지도 않고, 스택의 탑과 i가 같다면
            stack.pop()

    print(f"#{tc} {len(stack)}")