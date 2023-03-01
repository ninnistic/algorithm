# 이건 그냥 교재에서 조합만드는거 보고 따라함..
def dfs(elements, start, k):
    if k == 0:
        result.append(elements[:])
        return
    for i in range(start, c+1):
        if i < len(letters):
            elements.append(letters[i])
            dfs(elements, i+1, k-1)
            elements.pop()

l, c = map(int, input().split()) # l = 만들려는 문자열의 길이, c = 주어진 소문자들의 길이
letters = sorted(input().split())
result = []
vowels = ['a', 'e', 'i', 'o', 'u']
# print(letters)

dfs([], 0, l)
for i in range(len(result)):
    count = 0
    for letter in result[i]:
        if letter in vowels:
            count += 1

    if count >= 1 and count <= l - 2:
        print(''.join(result[i]))