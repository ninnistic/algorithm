def solution(numbers):
    max_value = 0
    for i in range(len(numbers)-1):
        for j in range(1, len(numbers)):
            if numbers[i] * numbers[j] > max_value:
                max_value = numbers[i] * numbers[j]
                print(max_value)
    return max_value


numbers = [0, 31, 24, 10, 1, 9]

solution(numbers)
