def solution(land):
    def dfs(row,col,visited,land,alpha,dic):
        st = [(row,col)]
        visited[row][col] = True
        land[row][col] = chr(alpha)
        
        while st:
            r,c = st.pop()
            
            for dr,dc in [(0,1),(1,0),(-1,0),(0,-1)]:
                newR = r + dr
                newC = c + dc
                
                if 0<=newR<len(land) and 0<=newC<len(land[0]) and not visited[newR][newC] and land[newR][newC] == 1:
                    st.append((newR,newC))
                    visited[newR][newC] = True
                    land[newR][newC] = chr(alpha)
                    dic[chr(alpha)] += 1
            
    answer = 0
    dic = {}
    visited = [[False] * len(land[0]) for _ in range(len(land))]
    alpha = ord('A')
    for row in range(len(land)):
        for col in range(len(land[0])):
            if not visited[row][col] and land[row][col] == 1:
                dic[chr(alpha)] = 1
                dfs(row,col,visited,land,alpha,dic)
                alpha += 1
    
    # print(land)
    # print(dic)
    
    maxV = 0
    for c in range(len(land[0])):
        out = []
        oil = 0
        for r in range(len(land)):
            if land[r][c] != 0 and land[r][c] not in out:
                out.append(land[r][c])
                oil += dic[land[r][c]]
        if oil >= maxV:
            maxV = oil
                
    answer = maxV
    return answer