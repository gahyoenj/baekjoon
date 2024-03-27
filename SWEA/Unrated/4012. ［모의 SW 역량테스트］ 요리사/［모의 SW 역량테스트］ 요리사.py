def combi(n,A,B):
    global minV
    if n == N:
        if len(A) == N//2:
            a = 0
            b =0
            for i in range(N//2):
                for j in range(N//2):
                    a += food[A[i]][A[j]]
                    b += food[B[i]][B[j]]
            minV = min(minV,abs(a-b))
        return
    
    combi(n+1,A+[n],B)  # A에 식재료 추가
    combi(n+1,A,B+[n])  # B에 식재료 추가

T= int(input())
for tc in range(T):
    N = int(input())
    food = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    minV = 21e9
    A = []
    B = []
    combi(0,A,B)
    print(f'#{tc+1} {minV}')