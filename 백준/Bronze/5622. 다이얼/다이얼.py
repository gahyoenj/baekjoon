word = list(map(str, input()))
for idx in range(len(word)):
    if word[idx] == 'A' or word[idx] == 'B' or word[idx] == 'C':
        word[idx] = 2
    elif word[idx] == 'D' or word[idx] == 'E' or word[idx] == 'F':
        word[idx] = 3
    elif word[idx] == 'G' or word[idx] == 'H' or word[idx] == 'I':
        word[idx] = 4
    elif word[idx] == 'J' or word[idx] == 'K' or word[idx] == 'L':
        word[idx] = 5
    elif word[idx] == 'M' or word[idx] == 'N' or word[idx] == 'O':
        word[idx] = 6
    elif word[idx] == 'P' or word[idx] == 'Q' or word[idx] == 'R' or word[idx] == 'S':
        word[idx] = 7
    elif word[idx] == 'T' or word[idx] == 'U' or word[idx] == 'V':
        word[idx] = 8
    else:
        word[idx] = 9
sumV = sum(word)
result = sumV + len(word)
print(result)