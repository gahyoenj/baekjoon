import sys
input = sys.stdin.readline
from itertools import combinations
T = int(input())

for _ in range(T):
    n = int(input())
    mbti = list(input().split())
    minV = 10000
    if len(mbti) >=33:
        # print(set(mbti))
        print(0)
    else:
        for case in combinations(mbti,3):
            three = 0
            # for two in combinations(case,2):
            #     # print(two)
            #     dis = 0
            #     for idx in range(4):
            #         if two[0][idx] != two[1][idx]:
            #             dis += 1
            #     three += dis
            for idx in range(4):
                if case[0][idx] != case[1][idx]:
                    three += 1

                if case[1][idx] != case[2][idx]:
                    three += 1

                if case[2][idx] != case[0][idx]:
                    three += 1
            if three < minV:
                minV = three
        print(minV)