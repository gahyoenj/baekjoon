def solution(array, commands):
    answer = []
    for i,j,idx in commands:
        arr = array[i-1:j]
        arr.sort()
        print(arr)
        answer.append(arr[idx-1])
    return answer