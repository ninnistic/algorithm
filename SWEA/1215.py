def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] == word[-1-i]:
            return True
    return False


for tc in range(1, 11):
    counts = 0
    board = [list(input()) for _ in range(8)]

    for i in range(8):
        for j in range(8):

    print(f"#{tc} {counts}")
