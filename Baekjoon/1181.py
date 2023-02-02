N = int(input())  # 단어의 개수

word_set = set()
word_list = list()

for i in range(N):
    word = input()  # 단어를 N개의 줄에 걸쳐 하나씩 받음
    word_set.add(word)  # 애초에 set에 저장함

word_list = list(word_set)  # 다시 list로 변환한다.(sort쓰기 위해)
word_list.sort()    # abcd순으로 정렬
word_list.sort(key=len)  # 길이로 정렬

for i in word_list:
    print(i)
