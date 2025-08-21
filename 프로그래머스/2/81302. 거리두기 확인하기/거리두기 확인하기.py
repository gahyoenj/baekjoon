from collections import deque
def check(r1,c1,r2,c2,room):
    if abs(r1-r2) + abs(c1-c2) == 1:
        return False
    if r1 == r2:
        c = (c1+c2) // 2
        if room[r1][c] == 'O':
            return False
    elif c1 == c2:
        r = (r1+r2) // 2
        if room[r][c1] == 'O':
            return False
    else:
        if room[r1][c2] == 'O' or room[r2][c1] == 'O':
            return False
    
    return True

def solution(places):
    answer = []
    for room in places:
        keep = True
        person = deque([])
        for row in range(5):
            for col in range(5):
                if room[row][col] == 'P':
                    person.append((row,col))
        
        while person:
            p = person.popleft()
            r1 = p[0]
            c1 = p[1]
            for r2,c2 in person:
                if abs(r1-r2) + abs(c1-c2) <= 2:
                    if not check(r1,c1,r2,c2,room):
                        keep = False
                        break
                
        if keep:
            answer.append(1)
        else:
            answer.append(0)
    return answer