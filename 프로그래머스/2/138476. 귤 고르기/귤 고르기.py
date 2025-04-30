def solution(k, tangerine):
    answer = 0
    counts = {}
    for size in tangerine:
        if size in counts:
            counts[size] += 1
        else:
            counts[size] = 1

    cnt = sorted(counts.values(), reverse=True)

    total = 0
    for c in cnt:
        total += c
        answer += 1
        if total >= k:
            break

    return answer
