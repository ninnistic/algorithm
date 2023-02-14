def recursion(s, l, r):
    global cnt  # 전역 변수
    cnt += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l+1, r-1)


def isPalindrome(s):
    return recursion(s, 0, len(s)-1)


t = int(input())

for i in range(t):
    s = input()
    cnt = 0  # recursion 함수의 호출 횟수
    print(isPalindrome(s), cnt)
