from itertools import permutations
def calc(n1,n2,e):
    if e == "+":
        return n1+n2
    elif e == '-':
        return n1 - n2
    elif e == '*':
        return n1 * n2

def solution(expression):
    answer = 0
    operator = set()
    exp = []
    num = ''
    for e in expression:
        if not e.isdigit():
            operator.add(e)
            exp.append(int(num))
            exp.append(e)
            num = ''
        else:
            num += e
    if num:
        exp.append(int(num))
    
    
    print(exp)
    
    maxV = 0
        
    for p in permutations(operator,len(operator)):
        exp_arr = exp[:]
        arr = []
        for op in p:
            while exp_arr:
                e = exp_arr.pop(0)
                if e == op:
                    n1 = arr.pop()
                    n2 = exp_arr.pop(0)
                    num = calc(n1,n2,e)
                    arr.append(num)
                else:
                    arr.append(e)
            exp_arr = arr[:]
        result = exp_arr[-1]
        if maxV < abs(result):
            maxV = abs(result)
        
    answer = maxV
    return answer