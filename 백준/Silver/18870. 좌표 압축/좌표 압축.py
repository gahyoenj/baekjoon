N = int(input())

lst = list(map(int, input().split()))

arr = list(set(lst))

arr.sort()

dic = {}

for i in range(len(arr)):
    dic[arr[i]]=i

# print(dic)

for num in lst:
    print(dic[num], end=' ')