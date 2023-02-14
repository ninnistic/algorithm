for _ in range(1, 11):
    test_case = int(input())
    board = [list(map(int,input().split())) for _ in range(100)] # 100x100 사다리판 생성
    
    start_y = 99
    start_x = 