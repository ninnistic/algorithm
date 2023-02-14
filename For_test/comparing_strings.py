def naive_search(long, short):
    for i in range(len(long) - len(short) + 1):  # 긴 문자열 loop
        for j in range(len(short)):  # 짧은 문자열 loop
            if short[j] != long[i+j]:  # 긴 문자열과 짧은 문자열을 비교하는 동안 같지 않다면 break
                break
            if j == len(short) - 1:  # 그렇지 않고 j가 끝까지 돌게 된다면(일치한다는 뜻)
                return 1
    return 0


t = int(input())
for i in range(1, t+1):
    short = input()
    long = input()
    result = naive_search(long, short)

    print(f"#{i} {result}")
