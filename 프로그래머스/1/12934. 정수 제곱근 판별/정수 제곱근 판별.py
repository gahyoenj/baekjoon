def solution(n):
    answer = 0
    num = n**0.5
    if float(int(num)) == num:
        return (int(num)+1)**2
    else:
        return -1
    return answer