def solution(book_time):
    answer = 0
    
    for idx in range(len(book_time)):
        for i in range(2):
            h,m = book_time[idx][i].split(':')
            time = int(h) * 60 + int(m)
            book_time[idx][i] = time
    
    book_time.sort(key=lambda x:x[0])
    
    s,e = book_time.pop(0)
    
    room = [e+10]
    
    
    while book_time:
        s_t,e_t = book_time.pop(0)
        reserve = False
        
        for i in range(len(room)):
            if room[i] <= s_t:
                room[i] = e_t + 10
                reserve = True
                break
        
        if not reserve:
            room.append(e_t+10)
        
        room.sort()
                
    answer = len(room)
    return answer