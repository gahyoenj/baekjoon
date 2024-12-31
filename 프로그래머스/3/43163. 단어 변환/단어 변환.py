def diff(word,difword):
    diff = 0
    for i in range(len(word)):
        if word[i] != difword[i]:
            diff += 1
    return diff

def bfs(begin,target,words):
    visited = [False] * len(words)
    q = []
    q.append([begin,0])
    
    while q:
        word,dist = q.pop(0)
        # print(word,dist)
        
        if word == target:
            return dist
            # print(dist)
        
        for i in range(len(words)):
            if diff(word,words[i]) == 1 and not visited[i]:
                q.append([words[i],dist+1])
                visited[i] = True

def solution(begin, target, words):
    answer = 0
    if target in words:
        answer = bfs(begin,target,words)
    return answer