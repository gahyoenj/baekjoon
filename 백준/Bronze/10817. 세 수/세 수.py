A, B, C = list(map(int, input().split()))
if A <= B <= C or A >= B >= C:
  secondV = B
if B <= A <= C or B >= A >= C:
  secondV = A
if A <= C <= B or A >= C >= B:
  secondV = C
print(secondV)