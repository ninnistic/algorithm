code = list(input())
rank = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
nums = []
operator = []

for token in code:
    if token == '(':
        operator.append(token)
    elif token == ')':
        while operator[-1] != '(':
            nums.append(operator.pop())
        operator.pop() # '(' 제거

    elif token in '+-*/':
        if len(operator) == 0:
            operator.append(token)

        else:
            if rank[token] == rank[operator[-1]]:
                nums.append(operator.pop())
                operator.append(token)
            if rank[token] > rank[operator[-1]]:
                operator.append(token)
            if rank[token] < rank[operator[-1]]: # 넣을 연산자의 우선순위가 작은경우
                nums.append(operator.pop())
                while len(operator) > 0 and rank[token] <= rank[operator[-1]]:
                    nums.append(operator.pop())
                operator.append(token)
    else:
        nums.append(token)

    while len(operator) > 0:
        postfix.append(operator.pop())