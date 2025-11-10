def solution(absolutes, signs):
    answer = 0
    for idx in range(len(signs)):
        if not signs[idx]:
            absolutes[idx] = -1 * absolutes[idx]
        answer += absolutes[idx]
    return answer