# 저번에 풀어본 문제여서 교수님 풀이로 풀어봄
# 빨강(1번) 다음에는 파랑(2번)이 와야한다.
# => 즉 2번을 찾고 직전(prev)가 1번이면 answer ++;
# 그 후에 prev <- n 갱신

t = 10
for tc in range(1, t+1):
    n = int(input()) # 줄
    arr = [input().split() for _ in range(n)]
    ans = 0
    for st in zip(*arr):
        ans += "".join(st).replace('0','').count('12')

    print(f"#{tc} {ans}")
