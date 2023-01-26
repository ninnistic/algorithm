# 4. 2차원 List의 전체 합 구하기
# 정수로만 이루어진 2차원 list를 전달 받아 해당 list의 모든 요소들의 합을 반환하는
# all_list_sum 함수를 built-in 함수인 sum() 함수를 사용하지 않고 작성하시오.

my_list = [[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]


def all_list_sum(list):
    total = 0
    for i in range(len(my_list)):
        for j in range(len(my_list[i])):
            total += my_list[i][j]
    return total


print(all_list_sum(my_list))
