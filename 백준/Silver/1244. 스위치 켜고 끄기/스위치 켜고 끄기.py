def toggle(no):
    switch[no] = (switch[no]+1) % 2    # 1이면 0 0이면 1

def m_do(no):
    for idx in range(no,T+1,no):
        toggle(idx)

def f_do(no):
# 여학생 조건 변수 start,end 따로 잡아서 늘려가기
    toggle(no)
    start = no - 1
    end = no + 1
    while start >= 1 and end <= T and switch[start] == switch[end]:
        toggle(start)
        toggle(end)
        start -= 1
        end += 1

T = int(input())
switch = [-10000] + list(map(int, input().split()))
num = int(input())
for _ in range(num):
    sex, no = map(int,input().split())

    if sex == 1:
        m_do(no)
    else:
        f_do(no)
for idx in range(1,T+1,20):
    print(*switch[idx:idx+20])     