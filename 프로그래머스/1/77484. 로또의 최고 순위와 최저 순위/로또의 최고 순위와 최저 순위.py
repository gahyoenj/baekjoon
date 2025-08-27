def solution(lottos, win_nums):
    answer = []
    winning = 0
    rank = {6:1,5:2,4:3,3:4,2:5}
    for num in lottos:
        if num in win_nums:
            winning += 1
    
    unknown = lottos.count(0)

    maxV = winning + unknown
    minV = winning
    
    print(maxV,minV)
    
    if maxV >=2:
        answer.append(rank[maxV])
    
    elif maxV < 2:
        answer.append(6)
    
    if minV >= 2:
        answer.append(rank[minV])
    else:
        answer.append(6)
    return answer