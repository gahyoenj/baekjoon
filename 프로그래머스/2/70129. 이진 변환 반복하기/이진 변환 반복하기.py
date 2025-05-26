def solution(s):
    answer = []
    ans = 0
    cnt = 0
    while s != "1":
        # print(s)
        cnt += 1
        before = len(s)

        zero = s.count("0")

        ans += zero
        result = before - zero

        s = bin(result)[2:]

    answer = [cnt, ans]
    return answer
