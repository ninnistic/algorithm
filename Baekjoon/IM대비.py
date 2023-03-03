'''
출력예시
#1 2
#2 -1
#3 1
#4 2
#5 1
'''
# tc 빼고
n, k_min, k_max = map(int, input().split())
scores = list(map(int, input().split()))
scores.sort()
# [3, 4, 5, 5, 5]
a = b = c = [] # 빈 배열 만들기 a반 : t2 이상, b반 : t1이상, c반 : t1 미만
res = [] # 결과를 넣어줄 빈 배열
t1 = t2 = 0

min_nun = min(scores)
max_num = max(scores)

print(scores.count(t1))


# #반 나누기
# for i in scores:
#     if i >= t2:
#         a.append(i)
#     elif t2 > i >= t1:
#         b.append(i)
#     elif t1 > i:
#         c.append(i)
#
# # 분반별 최소인원 최대인원 만족하는지 확인하기 아니면 print(-1) 해야함
#
# if k_min <= len(a) <= k_max and k_min <= len(b) <= k_max and k_min <= len(c) <=k_max:
#     res.append(len(a))
#     res.append(len(b))
#     res.append(len(c))
#     print(max(res)-min(res))
# else:
#     print(-1)


