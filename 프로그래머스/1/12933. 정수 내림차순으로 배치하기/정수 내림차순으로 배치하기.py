def solution(n):
    answer = ''
    num = []
    n = str(n)
    for number in n:
        num.append(number)
    num.sort(reverse=True)
    for number in num:
        answer += number
    return int(answer)