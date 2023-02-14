# 그룹 단어 체커

n = int(input())

counts = 0
group_word = 0

for _ in range(1, n+1):
    word = list(input())
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            next_word = word[j+1:]
            for k in range(len(next_word)):
                if word[j] == next_word[k]:
                    counts += 1
    if counts == 0:
        group_word += 1
    counts = 0 
print(group_word)

