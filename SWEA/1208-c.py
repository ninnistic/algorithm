
def get_max_idx():
    max_value = 0
    max_idx = -1
    for i in range(len(boxes)):
        if boxes[i] > max_value:
            max_value = boxes[i]
            max_idx = i  # max를 구하면서, 갱신되는 시점의 idx까지 저장함.
    return max_idx


def get_min_idx():
    min_value = 987654321
    min_idx = -1
    for i in range(len(boxes)):
        if boxes[i] < min_value:
            min_value = boxes[i]
            min_idx = i
    return min_idx


for i in range(1, 11):
    n = int(input())  # 덤프 힛수
    boxes = list(map(int, input().split()))
    for i in range(n):
        boxes[get_max_idx()] -= 1
        boxes[get_min_idx()] += 1

    result = boxes[get_max_idx()] - boxes[get_min_idx()]
    print(f'#{i} {result}')
