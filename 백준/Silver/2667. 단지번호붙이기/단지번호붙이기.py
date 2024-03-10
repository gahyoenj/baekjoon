def dfs(row,col):
    global cnt
    global visited
    st = []
    st.append((row,col))

    visited[row][col] = True

    while st:
        vr,vc = st.pop()


        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            newR = vr + dr
            newC = vc + dc
            if 0<= newR<N and 0<= newC<N and arr[newR][newC] == 1 and not visited[newR][newC]:
                cnt += 1
                st.append((newR,newC))
                visited[newR][newC]= True
                # dfs(newR,newC)
    return cnt

    # if row <0 or row>=N or col <0 or col >= N:
    #     return
    #
    # if arr[row][col] == 1:
    #     global cnt
    #     cnt += 1
    #     arr[row][col] = 0
    #     for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
    #         newR = row + dr
    #         newC = col + dc
    #         dfs(newR,newC)


N = int(input())
arr = [list(map(int,input())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
lst = []
cnt = 1
for row in range(N):
    for col in range(N):
        if arr[row][col] == 1 and not visited[row][col]:
            dfs(row,col)
            lst.append(cnt)
            cnt = 1
# print(row,col)

lst.sort()

print(len(lst))
for num in lst:
    print(num)