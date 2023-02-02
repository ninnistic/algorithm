import sys

N, K = map(int, sys.stdin.readline().split())
num = list(str(sys.stdin.readline()))
count = 0

for i in range(len(num)-1):
    for j in range(i+1, i+1+K-count):
        if int(num[i]) < int(num[j]):
            num[i] = -1
            count += 1
            break

a = 1
while count < K:
    num[-a] = -1
    count += 1
    a += 1

while True:
    try:
        num.remove(-1)
    except:
        break

num = "".join(num)
print(num)
