def cnt_one(n):
    if n < 0:
        return 0
    cnt = 0
    bit = 1
    nextBit = 2
    while bit <= n+1:
        cnt += (n // nextBit) * bit
        if (n % nextBit) >= bit:
            cnt += (n % nextBit - bit + 1)
        bit = nextBit
        nextBit *=2
    return cnt

A,B = map(int,input().split())
print(cnt_one(B)-cnt_one(A-1))

