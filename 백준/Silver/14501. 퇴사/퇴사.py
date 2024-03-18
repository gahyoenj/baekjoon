def counsel(day,total):
    global maxV
    if day == N:
        if maxV < total:
            maxV = total
        return

    if day + lst[day][0] <= N:
        counsel(day+lst[day][0],total+lst[day][1])


    counsel(day+1,total)


N = int(input())

lst = []
for _ in range(N):
    Ti,Pi = map(int, input().split())
    lst.append([Ti,Pi])

maxV = 0
counsel(0,0)
print(maxV)