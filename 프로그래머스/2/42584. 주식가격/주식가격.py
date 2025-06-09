def solution(prices):
    answer = []
    idx = len(prices)
    for i in range(idx-1):
        cnt = 0
        for j in range(1, idx-i):
            if prices[i] <= prices[i+j]:
                cnt += 1
            
            else:
                cnt += 1
                break
        answer.append(cnt)
    answer.append(0)
    return answer