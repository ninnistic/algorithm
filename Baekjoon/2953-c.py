import sys

max_score = 0
score_list = []

for i in range(5):
    scores = sum(map(int, sys.stdin.readline().split()))
    score_list.append(scores)
    if scores > max_score:
        max_score = scores


print(score_list.index(max_score)+1, max_score)
