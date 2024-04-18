def inOrder(root):
    global value
    if root < 2**K:
        inOrder(root*2)
        # print(root)
        TREE[root-1] = arr[value]
        value += 1
        inOrder(root*2+1)


K = int(input())
TREE = [0] * (2**K-1)
arr = list(map(int, input().split()))
value = 0
inOrder(1)
# print(TREE)
for i in range(K):
    for j in range(2**i):
        print(TREE[(2**i-1)+j], end=' ')
    print()