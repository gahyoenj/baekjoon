from collections import deque
def solution(arr):
    answer = []
    arr = deque(arr)
    answer.append(arr.popleft())
    while arr:
        num = arr.popleft()
        if num != answer[-1]:
            answer.append(num)
    return answer