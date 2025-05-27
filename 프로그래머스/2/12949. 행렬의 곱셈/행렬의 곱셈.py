def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        arr = arr1[i]
        result = []
        for j in range(len(arr2[0])):
            ans = 0
            for k in range(len(arr1[0])):
                ans += arr[k] * arr2[k][j]
            result.append(ans)
        answer.append(result)
    return answer