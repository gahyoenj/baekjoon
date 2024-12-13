def solution(sizes):
    answer = 0
    w = []
    h = []
    for idx in range(len(sizes)):
        w.append(max(sizes[idx]))
        h.append(min(sizes[idx]))
    answer = max(w) * max(h)
    return answer