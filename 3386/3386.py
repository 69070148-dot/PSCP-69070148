"""Duplicate I"""

m = int(input())
n = int(input())

a = set()
b = set()

for _ in range(m):
    a.add(input())

for _ in range(n):
    b.add(input())

c = sorted(a & b, reverse=True)

if not c:
    print("Nope")
else:
    for x in c:
        print(x)
