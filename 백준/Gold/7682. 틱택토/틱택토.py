def check(arr):
    o_flag = False
    x_flag = False

    # 행과 열 체크
    for idx in range(3):
        if arr[idx][0] == arr[idx][1] == arr[idx][2]:
            if arr[idx][0] == 'O':
                o_flag = True
            elif arr[idx][0] == 'X':
                x_flag = True

        if arr[0][idx] == arr[1][idx] == arr[2][idx]:
            if arr[0][idx] == 'O':
                o_flag = True
            elif arr[0][idx] == 'X':
                x_flag = True

    # 대각선 체크
    if arr[0][0] == arr[1][1] == arr[2][2]:
        if arr[0][0] == 'O':
            o_flag = True
        elif arr[0][0] == 'X':
            x_flag = True

    if arr[2][0] == arr[1][1] == arr[0][2]:
        if arr[2][0] == 'O':
            o_flag = True
        elif arr[2][0] == 'X':
            x_flag = True

    return o_flag, x_flag


while True:
    t = input()
    if t == 'end':
        break

    x = t.count('X')
    o = t.count('O')
    tick = [list(t[i:i + 3]) for i in range(0, 9, 3)]

    o_flag, x_flag = check(tick)

    # 게임이 끝난 경우
    if not o_flag and not x_flag and x==5 and o==4:
        ans = 'valid'
    elif x_flag and o_flag:
        ans = 'invalid'
    elif o_flag and x == o:
        ans = 'valid'
    elif x_flag and x == o + 1:
        ans = 'valid'
    else:
        ans = 'invalid'

    print(ans)
