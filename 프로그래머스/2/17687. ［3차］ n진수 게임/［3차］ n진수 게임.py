def solution(n, t, m, p):
    answer = ''
    
    result = '0'
    
    sixteen = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
    
    for i in range(1,t*m):
        res = ''
        while i > 0:
            num = i % n
            if num >= 10:
                num = sixteen[num]

            res += str(num)
            i = i // n
        result += res[::-1]
    # print(result)
    
    for idx in range(p-1,t*m,m):
        answer += result[idx]
        
    return answer