import heapq
def solution(info, n, m):
    answer = 0
    minA = 2e10
    st = [(0,0,0)]
    visited = [[2e10]*m for _ in range(len(info)+1)]
    while st:
        idx,sumA,sumB = st.pop()
        
        if sumB >= m:
            continue
        
        if idx == len(info):
            if minA > sumA:
                minA = sumA
            continue
        if sumA > visited[idx][sumB]:
            continue
        
        a,b = info[idx]
        
        if sumA + a < visited[idx+1][sumB]:
            visited[idx+1][sumB] = sumA + a
            st.append((idx+1,sumA+a,sumB))
        
        if sumB + b < m and sumA < visited[idx+1][sumB]:
            visited[idx+1][sumB+b] = sumA
            st.append((idx+1,sumA,sumB+b))
            
    if minA >= n:
        return -1
    else:
        return minA