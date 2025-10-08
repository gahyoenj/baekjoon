from sys import setrecursionlimit
setrecursionlimit(10000)

def solution(nodeinfo):    
    answer = []
    for idx in range(len(nodeinfo)):
        nodeinfo[idx].append(idx+1)
    
    nodeinfo.sort(key=lambda x:(-x[1], x[0]))
    # print(nodeinfo)
    root = nodeinfo[0]
    
    G = [[0,0] for _ in range(len(nodeinfo)+1)]

    def find(nodes):
        if not nodes:
            return 0
        root = nodes[0]
        left = []
        right = []
        
        for n in nodes[1:]:
            if n[0] < root[0]:
                left.append(n)
            elif n[0] > root[0]:
                right.append(n)
        G[root[2]][0] = find(left)
        G[root[2]][1] = find(right)
        return root[2]
    
    root_num = find(nodeinfo)
    
    
    def preorder(node,pre):
        if node == 0:
            return
        pre.append(node)
        preorder(G[node][0],pre)
        preorder(G[node][1],pre)
        
        return pre
        
        
    def postorder(node,post):
        if node == 0:
            return
        postorder(G[node][0],post)
        postorder(G[node][1],post)
        post.append(node)
        
        return post
    
    
    
    answer.append(preorder(root[2],[]))
    answer.append(postorder(root[2],[]))
    
    
    return answer