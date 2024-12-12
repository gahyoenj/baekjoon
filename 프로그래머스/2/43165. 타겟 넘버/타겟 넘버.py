def dfs(numbers,target,deep,value):
    global answer
    
    if deep == len(numbers) and value == target:
        answer += 1
    elif deep == len(numbers):
        return
    
    if deep < len(numbers):
        dfs(numbers, target, deep + 1, value + numbers[deep])
        dfs(numbers, target, deep + 1, value - numbers[deep])
    
    
def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers,target,0,0)
    
    return answer