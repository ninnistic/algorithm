# 오른쪽에서 N개의 막대기를 본다
# 젤 큰 놈이 top에 있으면 1개 아니라면 stack으로 제거하며 count

import sys
input = sys.stdin.readline

stack = []
n = int(input())
cnt = 1

# 스택에 저장
for _ in range(n):
    stack.append(int(input()))

# 스택에서 top값을 먼저 꺼냄 ()
top = stack.pop()
for _ in range(n-1):
    # 그 다음값과 비교
    next_top = stack.pop()
    if top < next_top:
        top = next_top
        cnt += 1

print(cnt)
