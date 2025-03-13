n = int(input())

word = {}
first = {}
for _ in range(n):
    w = input()


    if w[:2] not in word:
        word[w[:2]] = []

    word[w[:2]].append(w)

    if w[0] not in first:
        first[w[0]] = []
    first[w[0]].append(w)


# print(word)
maxV = 0
S = ''
T = ''
for key,value in word.items():
    if len(value) >=2:

        for i in range(len(value) - 1):
            for j in range(i+1, len(value)):
                length = 0
                while length < len(value[i]) and length < len(value[j]) and value[i][length] == value[j][length]:
                    length += 1

                if length > maxV:
                    maxV = length
                    S = value[i]
                    T = value[j]

if S and T:
    print(S)
    print(T)

else:
    for key, value in first.items():
        if len(value) >= 2:

            for i in range(len(value) - 1):
                for j in range(i + 1, len(value)):
                    length = 0
                    while length < len(value[i]) and length < len(value[j]) and value[i][length] == value[j][length]:
                        length += 1

                    if length > maxV:
                        maxV = length
                        S = value[i]
                        T = value[j]
    print(S)
    print(T)