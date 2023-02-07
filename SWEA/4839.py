def binary_search(pages, target_page):
    counts = 0
    first_page = 1
    last_page = pages
    middle_page = int((first_page + last_page)/2)

    while target_page != middle_page:

        if target_page < middle_page:
            last_page = middle_page

        elif target_page > middle_page:
            first_page = middle_page

        middle_page = int((first_page + last_page)/2)
        counts += 1

    return counts


t = int(input())

for tc in range(1, t+1):
    pages, page_a, page_b = map(int, input().split())

    counts_a = binary_search(pages, page_a)
    counts_b = binary_search(pages, page_b)

    if counts_a == counts_b:
        print(f"#{tc} {'0'}")
    else:
        print(f"#{tc} {'A'}") if counts_a < counts_b else print(f"#{tc} {'B'}")
