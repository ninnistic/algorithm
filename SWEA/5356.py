t = int(input())

words = [input() for i in range(5)]

for j in range(5):
    down = ''.join([words[j][i] for i in range(5)])


print(down)
