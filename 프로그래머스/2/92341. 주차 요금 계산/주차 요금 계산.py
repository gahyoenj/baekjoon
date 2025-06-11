def calc(before,time,m,parking,num):
    before_h, before_m = map(int, before.split(":"))
    time_h,time_m = map(int,time.split(":"))
    if time_m < before_m:
        m = 60 + (time_m - before_m)
        time_h -= 1
    else:
        m = time_m - before_m
    h = time_h - before_h

    print(num, m , h)

    length = m + (h*60)

    print(num, length)

    if num in parking:
        parking[num].append(length)
    else:
        parking[num] = [length]

def solution(fees, records):
    answer = []
    record = {}
    parking = {}
    for r in records:
        time, num, state = r.split(" ")

        if num in record.keys():
            if record[num]:
                before = record[num].pop(0)
                m = 0
                calc(before,time,m,parking,num)
            
            else:
                record[num].append(time)
                
        else:
            record[num] = [time]
    

    for num in record:
        if record[num]:
            before = record[num].pop(0)
            m = 0
            time = "23:59"
            calc(before,time,m,parking,num)
    
    sorted_items = sorted(parking.items()) 

    parking = dict(sorted_items)
    
    for num in parking:
        time = 0
        fee = fees[1]
        for t in parking[num]:
            time += t
        
        if time > fees[0]:
            over = int((time - fees[0]) / fees[2])
            if (time - fees[0]) % fees[2] != 0:
                over += 1
            over_fee = over * fees[3]
            fee += over_fee
        
        answer.append(fee)
        
    
    
    return answer