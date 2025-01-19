str = input()
bomb = input()
stack = []

for idx in range(len(str)):
    stack.append(str[idx])
    if str[idx] == bomb[-1]:
        if''.join(stack[-len(bomb)::]) == bomb:
            for _ in range(len(bomb)):
                stack.pop()
if stack:
    print(''.join(stack))
else:
    print("FRULA")
