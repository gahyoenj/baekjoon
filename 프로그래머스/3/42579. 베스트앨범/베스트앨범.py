def solution(genres, plays):
    answer = []
    cnt = {}
    
    time = {}
    
    for g in genres:
        if g not in cnt.keys():
            cnt[g] = []
        
        if g not in time.keys():
            time[g] = 0
        
    
    for idx in  range(len(plays)):
        genre = genres[idx]
        play = plays[idx]
        cnt[genre].append((play,idx))
        time[genre] += play
    
    # print(cnt)
    
    t = dict(sorted(time.items(), key=lambda x: x[1], reverse=True))
    
    # print(t)
    
    for genre in t:
        c = 0
        cnt[genre].sort(key=lambda x: (-x[0], x[1]))

        for p in cnt[genre]:
            c += 1
            answer.append(p[1])
            if c == 2:
                break
    
    
    
    return answer