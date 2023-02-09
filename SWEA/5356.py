t = int(input())

words = list(input())

for i in range(5):
    down = ''.join([words[j][i] for j in range(5)])


print(down)
