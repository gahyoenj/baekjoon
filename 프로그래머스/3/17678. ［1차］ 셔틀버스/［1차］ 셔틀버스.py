def solution(n, t, m, timetable):
    answer = ''
    arr = []
    for table in timetable:
        time = 0
        hour,minitue = table.split(":")
        time = int(hour) * 60 + int(minitue)
        arr.append(time)
    arr.sort()
    
    times = []
    for i in range(540,540+t*n,t):
        times.append(i)

    for t in times[:-1]:
        cnt = 0
        while arr and arr[0] <= t and cnt < m:
            arr.pop(0)
            cnt += 1

    while arr and times[-1] < arr[-1]:
        arr.pop()
    
    late = 0
    if len(arr) < m:
        late = times[-1]
    else:
        late = arr[m-1] - 1
    
    H = str(late // 60)
    M = str(late % 60)
    if len(H) < 2:
        H = '0' + H
    if len(M) < 2:
        M = '0' + M
    
    answer = H + ":" + M
    return answer