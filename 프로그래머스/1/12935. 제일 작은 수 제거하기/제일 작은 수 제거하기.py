import heapq
def solution(arr):
    answer = []
    if len(arr) <= 1:
        answer = [-1]
    else:
        minV = min(arr)
        arr.remove(minV)
        answer = arr
    return answer