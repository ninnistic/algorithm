def dfs(elements, start, k):
    if k == 0:
        result.append(elements[:])
        return
    for i in range(start, c + 1):
        if i < len(letters):
            elements.append(letters[i])
            dfs(elements, i + 1, k - 1)
            elements.pop()


l, c = map(int, input().split())  # l = 만들려는 문자열의 길이, c = 주어진 소문자들의 길이
letters = sorted(input().split())  # 사전순이므로
result = []
consonants = 'bcdfghjklmnpqrstvwxyz'
vowels = 'aeiou'
# 처음에 빈 배열을 넣고, 시작점은 0 으로 잡고 만들려는 문자열의 길이만큼 넣고 시작
dfs([], 0, l)
for i in range(len(result)):
    c_count = 0
    v_count = 0
    for j in result[i]:
        if j in vowels :
            v_count += 1
        if j in consonants:
            c_count += 1
        if c_count >= 1 and v_count >= 2:
            print(''.join(result[i]))
            break
