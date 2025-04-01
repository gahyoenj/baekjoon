T = int(input())

def post(pre,ino):
    if not pre:
        return []
    root = pre[0]
    idx = ino.index(root)

    left = post(pre[1:idx+1],ino[:idx])
    right = post(pre[idx+1:],ino[idx+1:])
    return left + right + [root]


for _ in range(T):

    N = int(input())

    pre = list(map(int,input().split()))
    ino = list(map(int,input().split()))

    ans = post(pre,ino)
    print(*ans)