# 국어 점수가 감소하는 순서로
# 국어가 같으면 영어점수가 증가하는 순서로
# 국어점수 영어점수가 같으면 수학점수가 감소하는 순서로
# 모든 점수가 같으면 이름이 사전순으로 증가하는 순서로 (대문자 > 소문자)
# 버블정렬로 안풀립디다..


n = int(input())
scores = []

for i in range(n):
    score = list(map(str, input().split()))
    scores.append([score[0], int(score[1]), int(score[2]), int(score[3])])

scores.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in scores:
    print(i[0])
