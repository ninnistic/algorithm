n = int(input())

book_dict = {}
best_seller = []

for _ in range(n):
    book = input()
    if book not in book_dict:
        book_dict[book] = 1
    else:
        book_dict[book] += 1
for key, value in book_dict.items():
    if value == max(book_dict.values()):
        best_seller.append(key)
best_seller.sort()
print(best_seller[0])
