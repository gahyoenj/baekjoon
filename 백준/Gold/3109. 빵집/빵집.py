def dfs(r,c):
    if c == C-1:
        return True

    for dr,dc in [(-1,1),(0,1),(1,1)]:
        newR = r + dr
        newC = c + dc

        if 0<= newR < R and 0<=newC < C and bakery[newR][newC] == '.':
            bakery[newR][newC] = 'X'
            if dfs(newR,newC):
                return True
    return False


R,C = map(int,input().split())

bakery = [list(input()) for _ in range(R)]

cnt = 0
for i in range(R):
    if dfs(i,0):
        cnt+= 1

print(cnt)