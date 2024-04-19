def preorder(root):
    print(root,end='')
    i = ord(root) - ord('A')
    if G[i][0]:
        preorder(G[i][0])
    if G[i][1]:
        preorder(G[i][1])

def inorder(root):
    i = ord(root) - ord('A')
    if G[i][0]:
        inorder(G[i][0])
    print(root, end='')
    if G[i][1]:
        inorder(G[i][1])

def postorder(root):
    i = ord(root) - ord('A')
    if G[i][0]:
        postorder(G[i][0])
    if G[i][1]:
        postorder(G[i][1])
    print(root, end='')


N = int(input())
G = [[] for _ in range(N)]

for _ in range(N):
    node, left,right = input().split()
    i = ord(node) - ord('A')
    if left.isupper():
        G[i].append(left)
    if left.isupper() == False:
        G[i].append(0)
    if right.isupper():
        G[i].append(right)
    if right.isupper() == False:
        G[i].append(0)

# print(G)
preorder('A')
print()
inorder('A')
print()
postorder('A')
# print(ord('A'))