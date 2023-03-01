heights = [int(input()) for _ in range(9)]
heights.sort()
total = sum(heights)

first = 0
second = 0

# 0번부터 8번까지 => total 9명
for i in range(9):  # 0번부터 7번까지
    for j in range(i+1, 9): # 1번부터 8번까지
        if total - heights[i] - heights[j] == 100:
            first = heights[i]
            second = heights[j]

heights.remove(first)
heights.remove(second)

for i in heights:
    print(i)



