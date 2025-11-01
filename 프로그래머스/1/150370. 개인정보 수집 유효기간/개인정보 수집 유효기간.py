def solution(today, terms, privacies):
    answer = []
    period = {}
    year,month,day = today.split('.')
    now = year+month+day

    for term in terms:
        t,m = term.split()
        period[t] = int(m)
    for idx,privacy in enumerate(privacies):
        date,t = privacy.split()
        y,m,d = map(int,date.split('.'))
        m += period[t]
        d -= 1
        while m > 12:
            y += 1
            m -= 12
        if d <= 0:
            d = 28
            m -= 1
        y = str(y)
        m = str(m)
        d = str(d)
        if len(m) < 2:
            m = '0' + m
        if len(d) < 2:
            d = '0' + d
        check = y+m+d
        if int(check) < int(now):
            answer.append(idx+1)
    return answer