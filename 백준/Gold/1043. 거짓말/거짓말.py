N, M = map(int, input().split())
arr = list(map(int, input().split()))

if arr[0] == 0:
    print(M)
else:
    know = []
    for person in arr[1:]:
        know.append(person)

    party = []
    for _ in range(M):
        lst = list(map(int, input().split()))
        party.append(lst[1:])

    changed = True
    while changed:
        changed = False
        for p in party:
            has_known = False
            for person in p:
                if person in know:
                    has_known = True
                    break
            if has_known:
                for person in p:
                    if person not in know:
                        know.append(person)
                        changed = True


    can_lie = 0
    for p in party:

        has_known = False
        for person in p:
            if person in know:
                has_known = True
                break
        if not has_known:
            can_lie += 1

    print(can_lie)
