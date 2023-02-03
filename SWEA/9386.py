t = int(input())

# 테스트 케이스
for tc in range(1, t+1):
    n = int(input())  # 수열의 길이
    nums = list(map(int, input()))  # 주어진 수열
    numbers = nums + [0]  # 한 칸 늘림

    num_list = []
    result = 0
    point = 0

    while point < n+1:    # 수열의 길이까지
        if numbers[point] == 1:  # 만약 수열이 1을 만난다면
            result += 1  # result += 1을 해주고
            point += 1         # 위치를 +1 해준다.
        else:
            num_list.append(result)  # 0을 만난다면 지금까지의 값을 저장하고
            result = 0        # result를 0으로 초기화해준다음
            point += 1        # 위치를 +1 옮겨준다.
    print(f"#{tc} {max(num_list)}")
