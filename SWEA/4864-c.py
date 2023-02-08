def get_length(word):
    length = 0
    for i in word:
        length += 1
    return length


t = int(input())

for tc in range(1, t+1):
    str_1 = input()
    str_2 = input()
    length_1 = get_length(str_1)
    length_2 = get_length(str_2)
    result = 0
    for i in range(length_2 - length_1 + 1):
        if str_2[i: i + length_1] == str_1[0:]:
            result += 1

    print(f"#{tc} {result}")
