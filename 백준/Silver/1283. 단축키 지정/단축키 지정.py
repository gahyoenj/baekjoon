N = int(input())
word = []

for _ in range(N):
    w = input()
    char = w.split(' ')
    find = False
    for i in range(len(char)):
        check = char[i][0].upper()
        if check not in word:
            word.append(check)
            char[i] = '[' + char[i][0] + ']' + char[i][1:]
            find = True
            answer = " ".join(char)
            print(answer)
            break
    if not find:
        for idx in range(1,len(w)):
            if w[idx] == " ": continue
            check = w[idx].upper()
            if check not in word:
                word.append(check)
                answer = w[:idx] + '[' + w[idx] +']' + w[idx+1:]
                print(answer)
                find = True
                break

    if not find:
        print(w)