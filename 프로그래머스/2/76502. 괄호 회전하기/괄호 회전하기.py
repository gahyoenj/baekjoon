def check(s):
    pair = {')':'(', ']':'[', '}':'{'}
    if s[0] in pair.keys():
        return False
    st = []
    while s:
        paren = s.pop(0)
        if paren in pair.keys() and st:
            if st[-1] == pair[paren]:
                st.pop()
            else:
                return False
        else:
            st.append(paren)
    if not st:
        return True
    else:
        return False


def rotate(s,n):
    if n > 0:
        s = s[n:] + s[:n]
    
    return s
    
def solution(s):
    answer = 0
    arr = []
    for p in s:
        arr.append(p)
    for i in range(len(s)):
        string = rotate(arr,i)
        
        # print(string)
        if check(string[:]):
            answer += 1
    return answer