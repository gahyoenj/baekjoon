N = int(input())
arr = list(map(int, input().split()))
student = []
for idx in range(len(arr)):
    num = arr[idx]
    student.insert(idx-num,idx+1)

print(*student)

