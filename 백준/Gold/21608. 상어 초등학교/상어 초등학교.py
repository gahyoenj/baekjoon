def check(row,col,like):
    global friends,blank
    for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
        newR = row + dr
        newC = col + dc
        if 0<=newR<N and 0<=newC<N:
            if seat[newR][newC] in like:
                friends += 1
            if seat[newR][newC] == 0:
                blank += 1

N = int(input())
likes = [[] for _ in range(N**2+1)]
seat = [[0] * N for _ in range(N)]
for _ in range(N**2):
    lst = list(map(int, input().split()))
    student = lst[0]
    like = lst[1:]
    likes[student].append(like)
    place = []
    maxV = 0
    close = 0   # 인접한 자리 개수
    for row in range(N):
        for col in range(N):
            if seat[row][col] == 0:
                friends = 0   # 인접한 좋아하는 학생
                blank = 0     # 인접한 빈칸
                check(row,col,like)
                # print(friends,blank)
                place.append([friends,blank,row,col])

    place.sort(key=lambda x: (-x[0],-x[1],x[2],x[3]))  # 좋아하는 학생 -> 빈칸 -> 행 작은순
    # print(place)
    seat[place[0][2]][place[0][3]] = student
# print(likes)
# print(seat)
ans = 0
for row in range(N):
    for col in range(N):
        stu = seat[row][col]
        cnt = 0
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            newR = row + dr
            newC = col + dc
            if 0<=newR<N and 0<=newC<N:
                if seat[newR][newC] in likes[stu][0]:
                    cnt += 1
        if cnt == 1:
            ans += 1
        if cnt == 2:
            ans += 10
        if cnt == 3:
            ans += 100
        if cnt == 4:
            ans += 1000
print(ans)