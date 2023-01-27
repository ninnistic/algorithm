# 6. 내 이름은 몇일까?
# 문자열을 전달 받아 해당 문자열의 각 문자에 대응되는 아스키 숫자들의
# 합을 반환하는 get_secret_number 함수를 작성하시오.
# 단, 문자열은 A~Z, a~z로만 구성되어 있다.

word = 'happy'


def get_secret_number(char):
    total = 0
    for i in char:
        total += ord(i)
    return total


print(get_secret_number(word))  # 546
