def solution(s):
    answer = True
    stack = []
    for par in s:
        if par == "(":
            stack.append(par)
        elif stack:  
            stack.pop()  
        else:
            answer = False
    if stack:
        answer = False
    return answer