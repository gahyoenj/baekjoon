from itertools import permutations

def solution(k, dungeons):
    answer = -1
    
    for arr in permutations(dungeons,len(dungeons)):
        cnt = 0
        current = k
        for minS, use in arr:
            if minS > current:
                break
            else:
                current -= use

                cnt += 1
        if cnt > answer:
            answer = cnt
    
    return answer