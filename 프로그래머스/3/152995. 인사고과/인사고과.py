def solution(scores):
    answer = 1
    wanho = scores[0]
    scores.sort(key=lambda x:(-x[0],x[1]))
    maxV = 0
    for score in scores:
        if wanho[0] < score[0] and wanho[1] < score[1]:
            return -1
        
        else:
            if sum(wanho) < score[0] + score[1] and maxV <= score[1]: 
                answer += 1
                maxV = score[1]
    return answer