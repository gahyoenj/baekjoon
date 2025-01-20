N = int(input())
lst = list(map(int, input().split()))
budget = int(input())

if sum(lst) <= budget:
    print(max(lst))
else:
    answer = 0
    start, end = 1, max(lst)

    while start <= end:
        mid = (start + end) // 2
        total = 0
        for num in lst:
            if num > mid:
                total += mid
            else:
                total += num
        if total <= budget:
            answer = mid
            start = mid + 1
        else:
            end = mid - 1
    print(answer)