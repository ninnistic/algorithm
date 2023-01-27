# 내 풀이.. 틀림
# T = int(input())

# for i in range(1, T + 1):
#     res = 0
#     input_num = list(map(int, input().split()))
#     for j in input_num:
#         res += j
# avg = round(res/len(input_num))
# print(f'#{i} {avg}')


T = int(input())

for test_case in range(1, T+1):
    a = list(map(int, input().split()))
    avg = round(sum(a)/len(a))
    print(f'#{test_case} {avg}')
