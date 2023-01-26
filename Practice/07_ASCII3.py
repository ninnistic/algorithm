# 7. 강한 이름
# 문자열 2개를 전달 받아 두 문자열의 각 문자에 대응되는 아스키 숫자들의 합을 비교하여
# 더 큰 합을 가진 문자열을 반환하는 get_strong_word 함수를 작성하시오.
# 단, 두 문자열의 아스키 숫자의 합이 같은 경우, 둘 다 반환하세요.

def get_strong_word(first, second):
    first_total = 0
    second_total = 0
    for i in first:
        first_total += ord(i)
    for j in second:
        second_total += ord(j)

    if first_total == second_total:
        return first, second
    return first if first_total > second_total else second


print(get_strong_word('abc', 'bcf'))
