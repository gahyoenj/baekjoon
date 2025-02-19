import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def post(start,end):
    if start > end:
        return
    mid = end + 1

    for i in range(start+1,end+1):
        if arr[i] > arr[start]:
            mid = i
            break
    post(start+1,mid-1) # 왼쪽 트리
    post(mid,end) # 오른쪽 트리
    print(arr[start]) #루트노드 출력


arr = []
while True:
    try:
        N = int(input())
        arr.append(N)
    except:
        break


post(0,len(arr)-1)