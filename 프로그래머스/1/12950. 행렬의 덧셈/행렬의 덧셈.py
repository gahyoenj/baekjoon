def solution(arr1, arr2):
    answer = []
    n = len(arr1)
    m = len(arr1[0])
    for i in range(n):
        sumV = []
        for j in range(m):
            sumV.append(arr1[i][j]+arr2[i][j])
        answer.append(sumV)
    
    return answer