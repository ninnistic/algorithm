import sys

n, k = map(int, sys.stdin.readline())
circle = []
removed = []

for i in range(n):
    circle.append(str(i+1))
    removed.append(circle)
