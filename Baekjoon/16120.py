word = input()
stack = []

for letter in word:
    stack.append(letter)
    # 스택에서 뒤에서 4개가 ppap랑 동일하면 p만 남기고 팝팝팝 -> 반복
    if ''.join(stack[-4:]) == 'PPAP':
        stack.pop()
        stack.pop()
        stack.pop()

    # P만 남으면 PPAP이므로,
if stack == ['P']:
    print("PPAP")
else:
    print("NP")
