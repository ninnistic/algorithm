while True:

    N = int(input())  # 테스트 케이스 정수로 받기

    if N == 0:          # N 으로 0 이 들어오면 종료
        break

    else:               # word가 들어올 dict를 만들고
        word_dict = {}

    for _ in range(N):
        word = input()
        # 원래 단어와, lower을 적용한 단어를 key, value로 저장
        word_dict[word] = word.lower()

    # 원래 딕셔너리의 밸류를 리스트에 넣고 정렬함
    ordered_words = sorted(list(word_dict.values()))

    # value로 key찾기 귀찮아서 뒤집어줌
    reverse_dict = {v: k for k, v in word_dict.items()}

    print(reverse_dict.get(ordered_words[0]))   # 첫번째 단어 찾아줌
