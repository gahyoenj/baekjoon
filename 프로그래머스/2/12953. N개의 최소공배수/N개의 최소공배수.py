def find(n1,n2):
    div = 1
    for n in range(2,n2+1):
        if n1 % n == 0 and n2 % n == 0:
            div = n
    
    return div


def solution(arr):
    answer = 0
    arr.sort()
    ans = arr[0]
    for i in range(1,len(arr)):
        result = find(ans,arr[i])
        ans = (ans * arr[i]) // result
    
    answer = ans
    return answer