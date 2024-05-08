import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:
        i,j = q.popleft()

        if (abs(festivalx-i) + abs(festivaly-j) <= 1000):
            print('happy')
            return

        for k in range(n):
            if not visited[k]:
                if abs(store[k][0]-i) + abs(store[k][1]-j) <= 1000:
                    q.append([store[k][0],store[k][1]])
                    visited[k] = True

    print('sad')

t = int(input())
for _ in range(t):
    n = int(input())
    homex,homey = map(int, input().split())
    store = []
    for _ in range(n):
        x,y = map(int, input().split())
        store.append([x,y])
    festivalx,festivaly = map(int, input().split())
    # city = [[0]*(festivalx+1) for _ in range(festivaly+1)]
    #
    # for i,j in store:
    #     city[j][i] = 1
    # # print(city)
    # beer = 20
    visited = [False] * n
    bfs(homex,homey)