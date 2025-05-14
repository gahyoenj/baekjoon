def solution(gems):
    answer = []
    jewerly = set(gems)
    jewerly_type = {}
    start = 0
    end = 0
    minV = 2e19
    
    if len(gems) == len(jewerly):
        answer = [1, len(gems)]
    if len(jewerly) == 1:
        answer = [1,1]
        
    else:
    
        while end < len(gems):
            gem = gems[end]
            jewerly_type[gem] = jewerly_type.get(gem,0) + 1
            end += 1

            while len(jewerly_type) == len(jewerly):
                if end - start < minV:
                    minV = end - start
                    answer = [start+1, end]

                jewerly_type[gems[start]] -= 1
                if jewerly_type[gems[start]] == 0:
                    del jewerly_type[gems[start]]

                start += 1

    return answer