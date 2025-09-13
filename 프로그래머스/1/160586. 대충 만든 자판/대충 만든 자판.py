def solution(keymap, targets):
    answer = []
    key_dict = {}
    for key in keymap:
        for idx in range(len(key)):
            if key[idx] in key_dict:
                key_dict[key[idx]] = min(idx+1, key_dict[key[idx]])
            else:
                key_dict[key[idx]] = idx+1
    
    # print(key_dict)
    for target in targets:
        cnt = 0
        for t in target:
            if t in key_dict:
                cnt += key_dict[t]
            else:
                cnt = -1
                break
        answer.append(cnt)
    return answer