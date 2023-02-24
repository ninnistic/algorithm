# 어떤 방법을 사용 할 수 있지? -> 백 트래킹!!! 연습하자...ㅠ

def sequence(nums):
    if len(nums) == m:  # 만약에 nums의 길이가 m과 같아지면 프린트하고 종료
        print(*nums)
        return
    else:  # 아니라면 1부터 n+1까지(ex. n이 2라면 1,2를 보기위해~)
        for i in range(1, n+1):
            if i not in nums:  # 가지치기
                nums.append(i)
                sequence(nums)  # 1이 쌓이고 -> 2가 쌓이고 m과 개수가 같아지면 return으로 종료
                nums.pop()    # 그 후 미 실행 되었던 nums.pop() 실행 callstack에 쌓인 순서대로 pop


n, m = map(int, input().split())  # n = 1 부터 n까지, m = 한 줄에 출력되는 수열의 길이
nums = []
sequence(nums)
