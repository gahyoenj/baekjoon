def solution(plans):
    answer = []
    wait = []
    
    for idx in range(len(plans)):
        n,s,t = plans[idx]
        h,m = s.split(":")
        s = int(h) * 60 + int(m)
        t = int(t)
        plans[idx] = n,s,t
    
    plans.sort(key=lambda x:x[1])
    
    print(plans)

    current = 0
    while len(plans) >= 2:
        name,start,playtime = plans.pop(0)
        current = start
        next_start = plans[0][1]
        if start + playtime <= next_start:
            answer.append(name)
            current = start + playtime
        else:
            time = next_start - start
            start += time
            playtime -= time
            wait.append([name,start,playtime])
            current = start + time
        
        if wait:
            while wait and current <= next_start:
                wn,ws,wt = wait.pop()
                if current + wt <= next_start:
                    current += wt
                    answer.append(wn)
                else:
                    taken = (next_start - current)
                    current += taken
                    wt -= taken
                    wait.append([wn,ws,wt])
                    break      

    if plans:
        answer.append(plans[0][0])
    
    while wait:
        name,start,time = wait.pop()
        answer.append(name)
    
    # print(wait)
            
        
        
    return answer