def change(melody):
    return melody.replace("C#", "c").replace("D#", "d")\
                 .replace("F#", "f").replace("G#", "g")\
                 .replace("A#", "a").replace("E#", "e")\
                 .replace("B#", "b")

def solution(m, musicinfos):
    answer = ''
    
    music = []
    
    m = change(m)
    
    for idx in range(len(musicinfos)):
        musicinfo = musicinfos[idx]
        st,end,title,melody = musicinfo.split(',')
        
        melody = change(melody)
        
        stH, stM = st.split(':')
        endH, endM = end.split(':')
        
        minute = int(endM) - int(stM)
        houre = int(endH) - int(stH)
        
        time = minute + houre*60
        
        length = len(melody)
        
        q = time // length
        mod = time % length
        
        
        play = melody * q + melody[:mod]
        
        # print(play)
        
        if m in play:
            music.append((title,time,idx))
        
                    
    music.sort(key=lambda x:(-x[1],x[2]))
    
    if music:
        answer = music[0][0]
    else:
        answer = '(None)'
    
    return answer