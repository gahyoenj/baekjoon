def solution(p):
    answer = ''
    if not p:
        return ''
    left = right = 0
    for i in range(len(p)):
        if p[i] == '(':
            left += 1
        else:
            right += 1
        if left == right:
            u,v = p[:i+1], p[i+1:]
            break
    # print(u)
    # print(v)
    correct = True
    
    if u[0] != '(':
        correct = False
    else:
        st = [u[0]]
        for par in u[1:]:
            if par == '(':
                st.append(par)
            else:
                if st[-1] == '(':
                    st.pop()
        if st:
            correct = False
    
    if correct:
        return u + solution(v)
    else:
        newS = '(' + solution(v) + ')'
        for par in u[1:-1]:
            if par == '(':
                newS += ')'
            else:
                newS += '('
        return newS
        
    return answer