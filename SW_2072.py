# Clear

# T = int(input())
# acc = 0;
# for test_case in range(1, T + 1):
# 	if test_case % 2 :
#         acc += test_case
# print(#T, acc)


T = int(input())
for i in range(1, T + 1):
    res = 0  # Test Case마다 초기화
    a = list(map(int, input().split()))
    for x in a:
        if x % 2 == 1:
            res += x
    # else : # 짝수인 경우
        # continue
    print(f'#{i} {res}')
