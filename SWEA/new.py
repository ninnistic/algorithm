for i in range(1, 11):
    length, num = input().split()
    length = int(length)
    num_list = list(map(str, str(num)))

    j = 0
    while j < len(num_list) - 1:
        if num_list[j] == num_list[j+1]:
            num_list.pop(j)
            num_list.pop(j)
            j = 0
        j += 1

    result = ''.join(num_list)

    print(f"#{i} {result}")
