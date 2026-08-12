"""Brick Bridge"""

a = int(input())
b = int(input())
goal = int(input())

big = min(b, goal // 5)
small = goal - big * 5

if small <= a:
    print(small)
else:
    print(-1)
