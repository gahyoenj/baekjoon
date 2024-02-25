def self(n):
    s = list(str(n))
    for i in s:
        n += int(i)
    return n

lst = list(range(1,10001))

for n in range(1,10001):
    if self(n) in lst:
        lst.remove(self(n))

for x in lst:
    print(x)