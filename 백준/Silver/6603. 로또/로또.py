from itertools import combinations

while True:
        lst = list(map(int, input().split()))
        K = lst[0]
        if K == 0:
            break
        else:
            lotto = lst[1:K+1]
            # print(lotto)
            lotto = sorted(lotto)
            for data in combinations(lotto,6):
                print(*data)
            print()
