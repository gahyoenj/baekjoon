def solution(brown, yellow):
    answer = []
    a = 3
    size = brown + yellow
    while True:
        if size % a == 0:
            b = size // a
            if 2*a + 2*(b-2) == brown:
                answer.append(a)
                answer.append(b)
                break
        a += 1
    answer.sort(reverse=True)
    return answer