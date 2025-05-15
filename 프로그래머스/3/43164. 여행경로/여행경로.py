def dfs(now,route,answer,l):
    st = [now]
    
    
    while st:
        current = st[-1]


        if current in route.keys() and route[current]:
            next = route[current].pop(0)
            st.append(next)
        
        else:
            answer.append(st.pop())
        
        
        if len(answer) == l:
            break

                
def solution(tickets):
    answer = []
    route = {}
    for a,b in tickets:
        if a in route.keys():
            route[a].append(b)
        else:
            route[a] = [b]
    for lst in route.values():
        lst.sort()
    dfs('ICN',route,answer,len(tickets)+1)
    return answer[::-1]