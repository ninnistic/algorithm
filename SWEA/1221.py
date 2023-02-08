t = int(input())
numbers = {'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4, 'FIV': 5,
           'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9}

for _ in range(1, t+1):
    tc_num, length = map(int, input().strip('#').split())
    test_case = input().split()
