# 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면

# [그림1] 과 같이 ”YYYY/MM/DD”형식으로 출력하고,

# 날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.


# 연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며

# 일은 [표1] 과 같이, 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.

T = int(input())

for test_case in range(1, T+1):
    date = input()
    last_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    month = int(date[4:6])
    day = int(date[6:])
    if month > 12 or month < 1:
        print(f'#{test_case} "-1"')
    elif day == 0 or day > last_day[month-1]:
        print(f'#{test_case} "-1"')
    else:
        print(f'#{test_case} {date[:4]}/{date[4:6]}/{date[6:]} ')
