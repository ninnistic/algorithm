for i in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes.sort()  # 오름차순 정렬

    for num in range(dump):
        if boxes[-1] - boxes[0] <= 1:
            break
        boxes[0] += 1
        boxes[-1] -= 1
        boxes.sort()  # 다시 오름차순 정렬

    print(f"#{i} {boxes[-1]-boxes[0]}")
