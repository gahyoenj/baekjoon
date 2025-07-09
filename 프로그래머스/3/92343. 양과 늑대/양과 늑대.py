def solution(info, edges):
    answer = 0
    graph = [[] for _ in range(len(info))]
    
    for v1,v2 in edges:
        graph[v1].append(v2)
        # graph[v2].append(v1)
    
    st = [(graph[0],1,0)]
    
    while st:
        can, s, w = st.pop()
        
        answer = max(answer,s)
        
        for idx in range(len(can)):
            node = can[idx]
            ns, nw = s, w
            
            if info[node] == 0:
                ns += 1
            
            else:
                nw += 1
            
            if ns <= nw:
                continue
            
            nextC = can[:idx] + can[idx+1:]
            nextC += graph[node]
            
            st.append((nextC,ns,nw))
    
    return answer