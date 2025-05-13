def solution(routes):
    answer = 0
    routes.sort(key = lambda x:x[0])
    camera = routes[0][1]
    
    for lst in routes[1:]:
        if lst[0] > camera:
            camera = lst[1]
            answer += 1
        else:
            camera = min(camera, lst[1])
    return answer + 1