def solution(n):
    def hanoi(n,s,m,e):
        result = []
        if n == 1:
            return [[s,e]]

        result += hanoi(n-1,s,e,m)
        result.append([s,e])
        result += hanoi(n-1,m,s,e)
        return result
        
    
    return hanoi(n,1,2,3)