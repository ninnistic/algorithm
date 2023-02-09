
t = int(input())
for tc in range(1, t+1):
    word, command = map(str, input().split())
    counts = len(word)
    i = 0

    while i + len(command) <= len(word):
        if word[i : i + len(command)] == command:
            counts -= len(command)-1
            i = i+len(command)
        else:
            i = i+1
    print(f"#{tc} {counts}")