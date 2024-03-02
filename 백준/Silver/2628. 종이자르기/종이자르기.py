N, M = map(int, input().split())
width = [0,N]
height = [0,M]
T = int(input())    # 자르는 횟수
for i in range(1,T+1):
    x, size = map(int, input().split())
    if x == 1:
        width.append(size)
    else:
        height.append(size)
# print(width)
# print(height)
width.sort()
height.sort()
w_lst = []
h_lst = []
for i in range(len(width)-1):
    w_lst.append(width[i+1]-width[i])
for i in range(len(height)-1):
    h_lst.append(height[i+1]-height[i])
print(max(h_lst) * max(w_lst))
