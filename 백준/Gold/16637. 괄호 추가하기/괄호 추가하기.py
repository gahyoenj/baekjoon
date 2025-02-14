N = int(input())
calc = input()

q = []

for s in calc:
    if s.isdigit():
        q.append(int(s))
    else:
        q.append(s)

def calculate(a,op,b):
    if op == '+':
        num = a + b
    elif op == '-':
        num = a-b
    elif op == '*':
        num = a * b
    return num
    # print(num)
def dfs(idx,ans):
    global maxV
    if idx == N-1:
        maxV = max(maxV,ans)

    if idx + 4 < N:
        # print(q[idx+2],q[idx+3],q[idx+4])
        dfs(idx+4, calculate(ans,q[idx+1],calculate(q[idx+2],q[idx+3],q[idx+4])))

    if idx + 2 < N:
        dfs(idx+2, calculate(ans,q[idx+1],q[idx+2]))

maxV = -21e9
dfs(0,q[0])

print(maxV)