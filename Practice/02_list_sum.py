# 2. List의 합 구하기
# 정수로만 이루어진 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는
# list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

num_list = [1, 2, 3, 4, 5]


def list_sum(list):
    total = 0
    for i in list:
        total += i
    return total


print(list_sum(num_list))  # 15
