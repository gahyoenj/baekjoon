def solution(n, k):
    answer = 0
    num = ''
    if k == 8:
        num = oct(n)[2:]
    
    elif k == 10:
        num = str(int(n))
    
    else:
        while n > 0:
            n, mod = divmod(n, k)
            num += str(mod)
        num = num[::-1]
    
    s = num.split('0')
    for c in s:
        if c == '1' or c == '':
            continue
        else:
            c = int(c)
            check = False
            for i in range(2,int(c**0.5)+1):
                if c % i == 0:
                    check = True
                    break
            
            if not check:
                answer += 1
    return answer