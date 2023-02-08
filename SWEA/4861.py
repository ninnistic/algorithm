
def is_palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            return False
    return True


t = int(input())


for tc in range(1, t+1):
    # n x n 크기의 글자판, m = 회문의 길이
    n, m = map(int, input().split())

    # n개의 단어 받기
    texts = [input() for _ in range(n)]

    # 결과를 받을 비어있는 스트링
    result = ''

    for i in range(n):
        across = texts[i]  # 가로 단어 ex) ['abcde', 'efdaf', 'efefd' ... ]
        down = ''.join([texts[j][i] for j in range(n)])  # 세로 단어

        for j in range(n - m + 1):
            across_word = across[j: j+m]
            if is_palindrome(across_word) == True:
                result = across_word
                break

            down_word = down[j: j+m]
            if is_palindrome(down_word) == True:
                result = down_word
                break

        if result != '':
            break

    print(f"#{tc} {result}")
