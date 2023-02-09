# 전처리 함수
def pre_processing(pattern):
    next = [0] * len(pattern)
    j = 0  # 앞 글자
    for i in range(1, len(pattern)):  # 뒷 글자
        if pattern[i] == pattern[j]:
            next[i] = j + 1
            j += 1
        else:
            j = 0   # 다시 맨 앞부터 비교
            if pattern[i] != pattern[j]:
                next[i] = j + 1
                j += 1
    return next


def KMP(text, pattern):
    # 패턴 전처리
    pre_processing(pattern)
    pass


pattern_list = ["ZRO", "ONE", "TWO", "THR",
                "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]

t = int(input())
for i in range(t):
    tc, n = input().split()
    text = list(input().split())

    for i in range(10):
        for j in range(KMP(text, pattern_list[i])):
