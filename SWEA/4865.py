def max_value(arr):
    max_v = 0
    for i in arr:
        if i > max_v:
            max_v = i
    return max_v


t = int(input())

for tc in range(1, t+1):

    str1 = input()
    str2 = input()

    alphabets = set()
    counting = {}
    values = []

    for char in str1:       # str1로 입력받은 글자의 알파벳을 set에 넣어준다.
        alphabets.add(char)

    alphabets_list = list(alphabets)  # set을 list에 넣는다

    for char in str2:     # str2로 입력받은 글자들의 개수를 세기 위해
        if char not in counting:    # 딕셔너리에 넣는다
            counting[char] = 1
        else:
            counting[char] += 1

    for char in alphabets_list:   # counting 딕셔너리의 key를 set에있던 요소로 해서
        values.append(counting[char])  # 값을 리스트에 추가한다.

    print(f"#{tc}", max_value(values))  # 만든 max_value로 값을 찾는다.
