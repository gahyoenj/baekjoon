def solution(n, arr1, arr2):
    answer = []
    
    for idx in range(n):
        c = bin(arr1[idx] | arr2[idx])[2:]
        
        if len(c) != n:
            c = (n-len(c))*'0' + c
        
        
        result = ''
        for idx in range(n):
            if c[idx] == '1':
                result += '#'
            else:
                result += " "
        
        answer.append(result)

    
    return answer