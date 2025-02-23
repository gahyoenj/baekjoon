from collections import deque

N, K = map(int, input().split())
belt = list(map(int, input().split()))
belt = deque(belt)
robot = deque([False] * N)
cnt = 0
zero_count = 0

while zero_count < K:
    cnt += 1

    belt.rotate()
    robot.rotate()
    robot[-1] = False

    for i in range(N - 2, -1, -1):
        if robot[i] and not robot[i + 1] and belt[i + 1] > 0:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1
            if belt[i + 1] == 0:
                zero_count += 1

    robot[-1] = False


    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

        if belt[0] == 0:
            zero_count += 1

print(cnt)
