code_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5,
             '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
n, m = map(int, input().split())
codes = [input() for _ in range(n)]
for i in range(n):
