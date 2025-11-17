def solution(x):
    answer = True
    num = str(x)
    total = 0
    for s in num:
        total += int(s)
    if x % total == 0:
        return True
    else:
        return False
    return answer