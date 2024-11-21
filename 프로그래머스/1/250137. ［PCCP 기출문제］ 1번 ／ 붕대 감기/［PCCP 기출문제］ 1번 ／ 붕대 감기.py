def solution(bandage, health, attacks):
    sequence = 0
    answer = health
    last = attacks[-1][0]
    i = 0
    
    for t in range(last):
        if answer <=0 : return -1
        time = t + 1
        # if time : pass
        print(time,end=' ')
        
        if time == attacks[i][0]:
            answer -= attacks[i][1]
            sequence = 0
            i += 1
        
        else:
            sequence += 1
            if answer < health:
                if sequence == bandage[0]:
                    answer += bandage[2]
                    sequence = 0
        
                answer += bandage[1]
            
            else:
                answer = health
        print(answer)
    
    if answer <= 0:
        answer = -1
    return answer
            
                
        