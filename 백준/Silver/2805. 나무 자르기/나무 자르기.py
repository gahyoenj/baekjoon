def sol():
    start = 0
    end = max(tree)
    ans = 0

    while start <= end:
        mid = (start + end) // 2
        sum = 0

        for height in tree:
            if height > mid:
                sum += height - mid

        # 필요한 나무를 만족하는 경우
        if sum >= M:
            ans = mid  # 가능한 높이로 기록
            start = mid + 1  # 더 큰 높이에서 시도
        else:
            end = mid - 1  # 너무 많이 잘랐으니, 더 낮은 높이에서 시도

    return ans


N, M = map(int, input().split())
tree = list(map(int, input().split()))

print(sol())
