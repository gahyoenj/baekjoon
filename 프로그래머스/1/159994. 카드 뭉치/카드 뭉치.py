def solution(cards1, cards2, goal):
    answer = ''
    can = True
    for word in goal:
        if cards1 and word == cards1[0]:
            cards1.pop(0)
        elif cards2 and word == cards2[0]:
            cards2.pop(0)
        else:
            can = False
            break
    
    if can:
        answer = 'Yes'
    else:
        answer = 'No'
    return answer