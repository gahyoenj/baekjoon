n = int(input())
ball = input()

red = ball.count('R')
blue = n - red

if red == 0 or blue == 0:
    ans = 0

minV = 2e19
for color in 'RB':
    temp_r = ball.rstrip(color)
    cnt = temp_r.count(color)
    if cnt < minV:
        minV = cnt

    temp_l = ball.lstrip(color)
    cnt_l = temp_l.count(color)
    if cnt_l < minV:
        minV = cnt_l

print(minV)