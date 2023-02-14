def counting_sort(arr):
    output = [0] * len(arr)

    # 카운팅 정렬할 배열 초기화
    counts = [0] * 10

    # counts 배열에, 각 원소를 카운팅해 넣는다.
    for i in range(0, len(arr)):
        counts[arr[i]] += 1

    # counts 배열의 누적 합을 구한다.(앞 인덱스만큼을 계속 더함)
    for i in range(1, 10):
        counts[i] += counts[i-1]

    # 즉, counts는 각 원소들의 정렬됐을 때의 인덱스 정보를 담고 있다.
    # counts[arr[i]] = arr[i]의 값이 정렬 됐을 때, i의 위치중 가장 큰 번호 + 1
    # 기존 배열의 각 원소의 인덱스를 카운팅 배열에서 찾은 다음에
    # 정렬된배열(output)에 arr[i]의 값을 담아준다.
    # 즉, arr[i]가 정렬되었을 때의 index를 알기 위해서는 counts가 필요하다.
    # counts[arr[i]-1] == 정렬되었을 때 arr[i](값) 의 가장 큰 인덱스 정보.

    i = len(arr) - 1
    while i >= 0:
        output[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1
        i -= 1

    # 그 다음, 원래 arr배열에 정렬된 값을 넣어준다.
    for i in range(0, len(arr)):
        arr[i] = output[i]
