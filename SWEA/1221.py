t = int(input())

for i in range(1, t + 1):
    tc, n = input().split()
    n = int(n)
    num_list = ['ZRO', 'ONE', 'TWO', 'THR',
                'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
    num = list(map(str, input().split()))
    print(f'#{i}')

    for i in range(len(num_list)):
        for j in range(n):
            if num_list[i] == num[j]:
                print(num_list[i], end=' ')
