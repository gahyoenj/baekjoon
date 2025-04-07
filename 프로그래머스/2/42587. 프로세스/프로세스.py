def solution(priorities, location):
    answer = 0
    n = len(priorities)
    process = [chr(i) for i in range(65,65+n)]
    target = process[location]
    end = []
    while priorities:
        maxV = max(priorities)
        num = priorities.pop(0)
        pro = process.pop(0)
        if num >= maxV:
            end.append(pro)
            if pro == target:
                answer = len(end)
                break
        else:
            priorities.append(num)
            process.append(pro)
    print(end)
    return answer