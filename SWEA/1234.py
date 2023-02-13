for i in range(1, 11):
    length, num = input().split()
    length = int(length)
    num_list = list(map(str, str(num)))

    j = 0
    while j < len(num_list) - 1:
        for k in range(len(num_list) - 1):
            if num_list[k] == num_list[k+1]:
                num_list.pop(k)
                num_list.pop(k)
                j = 0
                break
            j += 1

    result = ''.join(num_list)

    print(f"#{i} {result}")
