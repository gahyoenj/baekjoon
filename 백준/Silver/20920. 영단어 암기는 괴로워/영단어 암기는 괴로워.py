import sys
input = sys.stdin.readline

N, M = map(int, input().split())

word_count = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


arr = list(word_count.items())
arr.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for word in arr:
    print(word[0])