T = int(input())

def make(now, sign, num, i, ans):
    if i == N:
        now += (sign*num)
        if now == 0:
            result.append(ans)
        return

    make(now,sign, num*10+(i+1), i+1, ans+" "+str(i+1))
    make(now+sign*num,1, i+1, i+1, ans+"+"+str(i+1))
    make(now+sign*num,-1, i+1, i+1, ans+"-"+str(i+1))

for _ in range(T):
    N = int(input())
    result = []
    make(0,1,1,1,"1")
    result.sort()
    print("\n".join(result))
    print()