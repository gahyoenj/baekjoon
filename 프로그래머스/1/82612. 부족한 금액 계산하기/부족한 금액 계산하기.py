def solution(price, money, count):
    answer = 0
    total = 0
    for cnt in range(1,count+1):
        total += price*cnt
    if total - money > 0:
        return total - money
    return answer