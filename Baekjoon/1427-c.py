n = list(input())
tmp = 0

for i in range(len(n)-1):
    for j in range(i+1, len(n)):
        if n[i] < n[j]:
            tmp = n[j]
            n[j] = n[i]
            n[i] = tmp
        else:
            continue

print(''.join(n))
