def solution(begin, end):
    answer = []
    for num in range(begin,end+1):
        if num == 1:
            answer.append(0)
            continue
        else:
            res = [1]
            for i in range(2,int(num**0.5)+1):
                if num % i == 0 and i <= 10000000:
                    res.append(i)
                    if num // i != num and num // i <= 10000000:
                        res.append(num//i)
                
            answer.append(max(res))
    return answer