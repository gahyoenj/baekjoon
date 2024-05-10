s = input()

n = (len(s) // 2) * 2
maxl = 0
for l in range(2, n+1,2):   # 행운의 티켓 길이 2N 이므로
    for idx in range(len(s)-l+1):
        lucky = s[idx:idx+l]
        # print(lucky)
        N = len(lucky)//2
        left = 0
        right = 0
        for x in lucky[:N]:
            left += int(x)
        for x in lucky[N::]:
            right += int(x)
        if left == right and len(lucky) > maxl:
            # print(lucky)
            maxl = len(lucky)
print(maxl)