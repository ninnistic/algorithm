import sys

N = int(sys.stdin.readline())
num = list(map(int, (sys.stdin.readline()).split()))
print(f"{min(num)} {max(num)}")
