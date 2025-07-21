def solution(picks, minerals):
    answer = 0
    
    stress = {'diamond':25,'iron':5, 'stone': 1}
    
    mineral_lst = []
    
    max_mines = sum(picks) * 5
    minerals = minerals[:max_mines]

    
    for i in range(0,len(minerals),5):
        w = 0
        for m in minerals[i:i+5]:
            w += stress[m]

        mineral_lst.append((minerals[i:i+5],w,i))
    
    mineral_lst.sort(key=lambda x:(-x[1],x[2]))

    
    while mineral_lst:
        if sum(picks) == 0:
            break
            

        
        if picks[0] != 0:
            answer += len(mineral_lst[0][0])
            picks[0] -= 1
            mineral_lst.pop(0)
        
        elif picks[1] != 0:
            dia = mineral_lst[0][0].count('diamond')
            answer += (dia*5) + len(mineral_lst[0][0]) - dia
            picks[1] -= 1
            mineral_lst.pop(0)
        
        else:
            dia = mineral_lst[0][0].count('diamond')
            iro = mineral_lst[0][0].count('iron')
            st = mineral_lst[0][0].count('stone')
            
            answer += (dia*25) + (iro*5) + st
            picks[2] -= 1
            
            mineral_lst.pop(0)
        
    
#     print(mineral_lst)
    return answer