def solution(n):
    answer = 0
    num = bin(n)
    cnt = num.count("1")
    current = n+1
    while True:
        current_bin = bin(current)
        if current_bin.count("1") == cnt:
            answer = current
            break
        current += 1
    return answer