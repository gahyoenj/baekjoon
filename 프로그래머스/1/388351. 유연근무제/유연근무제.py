def solution(schedules, timelogs, startday):
    answer = 0
    sat = (6 - startday) % 7
    sun = (sat + 1) % 7
    for idx in range(len(schedules)):
        timelog = timelogs[idx]
        sche = schedules[idx]
        h = sche // 100
        m = sche - (h*100)
        schedule = h * 60 + m
        late = False
        for idx,time in enumerate(timelog):
            hour = time // 100
            minute = time - (hour*100)
            work = hour * 60 + minute
            if idx == sat or idx == sun:
                continue
            if schedule + 10 < work:
                late = True
                break
        if not late:
            answer += 1

    return answer