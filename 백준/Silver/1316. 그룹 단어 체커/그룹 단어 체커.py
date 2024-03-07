N = int(input())
cnt = N
for _ in range(N):
    word = list(input())
    for idx in range(len(word)-1):
        if word[idx] == word[idx+1]:
            continue
        elif word[idx] in word[idx+1:]:
            cnt -= 1
            break

print(cnt)
