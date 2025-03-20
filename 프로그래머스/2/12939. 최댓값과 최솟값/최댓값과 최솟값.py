def solution(s):
    answer = ''
    num = s.split(' ')
    for idx in range(len(num)):
        num[idx] = int(num[idx])
    ans = ""
    ans += str(min(num))
    ans += " "
    ans += str(max(num))
    answer = ans
    return answer