def toggle(light):
    if light == 'Y':
        light = 'N'
    else:
        light = 'Y'
    return light


light = list(input())
light = [0] + light

# print(light)

cnt = 0

for idx in range(len(light)):
    if light[idx] == 'Y':
        for i in range(0,len(light)-idx,idx):
            light [idx+i] = toggle(light[idx+i])
        cnt += 1
if 'Y' in light:
    print(-1)
else:
    print(cnt)
