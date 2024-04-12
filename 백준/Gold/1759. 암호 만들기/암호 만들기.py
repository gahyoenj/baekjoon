def check(lst):
    v = 0
    c = 0
    for s in lst:
        if s in ['a','e','i','o','u']:
            v += 1
        else:
            c += 1
    # print(v,c)
    if v >= 1 and c >= 2:
        return True
    else:
        return False

def combi(k,s):
    if k == L:
        # print(result)
        if check(result):
            for a in result:
                print(a,end='')
            print()
        return


    for i in range(s,C):
        result[k] = arr[i]
        combi(k+1,i+1)

L, C = map(int,input().split())
arr = list(input().split())
arr.sort()
# print(arr)
result = [-1] * L
combi(0,0)