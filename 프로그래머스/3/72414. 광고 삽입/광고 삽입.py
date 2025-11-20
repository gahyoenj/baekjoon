def change(time):
    result = 0
    h,m,s = map(int,time.split(":"))
    result += (h*3600)
    result += (m*60)
    result += s
    return result
def exchange(time):
    if time < 10:
        return '0' + str(time)
    else:
        return str(time)
def solution(play_time, adv_time, logs):
    answer = ''
    play = change(play_time)
    adv = change(adv_time)
    dp = [0] * (play+1)
    for log in logs:
        start,end = log.split("-")
        s = change(start)
        e = change(end)
        dp[s] += 1
        dp[e] -= 1
    
    for time in range(1,play+1):
        dp[time] += dp[time-1]
    
    for t in range(1,play+1):
        dp[t] += dp[t-1]
        
    maxT = dp[adv-1]
    maxS = 0
    for start in range(1,play-adv+1):
        end = start + adv - 1
        total = dp[end] - dp[start-1]
        
        if total > maxT:
            maxT = total
            maxS = start
    hour = maxS // 3600
    minute = (maxS%3600) // 60
    second = (maxS%60)
    h,m,s = map(exchange,[hour,minute,second])
    answer = f'{h}:{m}:{s}'
    return answer