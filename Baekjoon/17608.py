# 오른쪽에서 N개의 막대기를 본다 = 즉 stack의 꼭대기에서 바라본다와 동일
# 스택의 top이 다른 것보다 작다 => 가장 큰값 - top
# 스택이 가장 큰 값이다 => top 반환
# sys 안쓰면 시간초과아아악...!
import sys

stack = []
n = int(input())
top = stack[-1]

for _ in range(n):
    stack.append(int(input()))

while
