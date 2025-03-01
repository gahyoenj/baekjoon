T = int(input())

for _ in range(T):
    w = input()
    n = int(input())
    found = False

    min_length = 2e29
    max_length = -1


    for char in set(w):
        word = []
        for i in range(len(w)):
            if w[i] == char:
                word.append(i)

        if len(word) >= n:
            for i in range(len(word)-n+1):
                length = word[i+n-1] - word[i] + 1
                min_length = min(min_length,length)
                max_length = max(max_length,length)
                found = True

    if found:
        print(min_length, max_length)
    else:
        print(-1)

