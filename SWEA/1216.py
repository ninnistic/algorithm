def check_palindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[-1-i]:
            return False
    return True


# 전체 board 배열 만들기
# 가로 회문 검사해서 넣기
# 세로 회문 검사해서 배열에 넣기
# 그 배열에서 가장 큰 값 찾기

# => 이 방식이 아니라, 가장 큰 값을 구하는 것이므로
# 가장 큰 값부터 찍어나가며 가로에서 가장 큰 값 세로에서 가장 큰 값을 구한다음에 비교한다.


def is_palindrome(arr):
    for i in range(100, 0, -1):  # 100부터 0까지 -1씩 줄어든다
        for j in range(101-i):  # j 는 100 - i
            for k in arr:   # k는 열을 움직이며 값을 찍음
                if check_palindrome(k[j: j + i]):
                    return i  # max 길이 구하기


for tc in range(10):
    t = int(input())

    row = [list(input()) for _ in range(100)]  # 가로

    vertical = [[row[j][i] for j in range(100)] for i in range(100)]  # 세로

    lst = row + vertical  # 가로 세로 한번에 같이 돌리기

    result = is_palindrome(lst)

    print(f"#{t} {result}")
