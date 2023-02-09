def is_palindrome(word):
    for i in range(len(word)//2):
        if word[i] == word[-1-i]:
            return True
    return False
