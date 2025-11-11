def solution(n, m, section):
    answer = 0
    current = 0
    for i in section:
        if i > current:
            answer += 1
            current = i + m -1
    return answer