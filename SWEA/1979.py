

# list comprehension 이라서 리스트안에 리스트가 저장된다. 2차원 입력값 list에 저장하기.


# [['0', '0', '1', '1', '1'],
# ['1', '1', '1', '1', '0'],
# ['0', '0', '1', '0', '0'],
# ['0', '1', '1', '1', '1'],
# ['1', '1', '1', '0', '1']] 2차원 배열은 이런 모양으로 이해하는게 좋다.

T = int(input())

for test_case in range(1, T+1):
    total = 0
    n, k = map(int, input().split())
    board = [input().split() for _ in range(n)]
    # 가로
    width = 0
    line = 0
    for line in board:
