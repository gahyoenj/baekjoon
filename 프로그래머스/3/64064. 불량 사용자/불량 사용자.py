from itertools import permutations
def solution(user_id, banned_id):
    answer = 0
    arr = []
    for perm in permutations(user_id,len(banned_id)):
        match = True
        for i in range(len(banned_id)):
            if len(perm[i]) != len(banned_id[i]):
                match = False
                break
            else:
                for idx in range(len(perm[i])):
                    if banned_id[i][idx] == '*':
                        continue
                    else:
                        if perm[i][idx] != banned_id[i][idx]:
                            match = False
                            break
        if match:
            if set(perm) not in arr:
                arr.append(set(perm))
    answer = len(arr)
    return answer