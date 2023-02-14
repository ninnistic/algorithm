# 찾으려는 문자열이 3개라면, 앞에서 2개를 갖다가 뒤에 붙임
# 찾으려는 문자열이 5개라면, 앞에서 4개를 갖다가 뒤에 붙임
# 즉 찾으려는 문자열이 k개라면 앞에서 k-1개를 갖다가 배열에 붙인다음 찾으면 된다.

target = input()  # 찾으려는 문자열
n = int(input())  # 입력 받을 줄 개수
k = len(target)  # 뒤에다 갖다 붙일 문자열의 길이를 위해 length 구하기
counts = 0

rings = [input() for _ in range(n)]
new_rings = []
for i in rings:
    ring = i + i[:k-1]
    new_rings.append(ring)

for ring in new_rings:
    for j in range(k):
        if ring[j: j+k] == target:
            counts += 1

print(counts)
