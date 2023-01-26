# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
import sys

N = int(sys.stdin.readline())

num_list = []
for i in range(N):
    num = int(sys.stdin.readline())
    num_list.append(num)

sorted_list = sorted(set(num_list))

for j in range(len(sorted_list)):
    print(sorted_list[j])
