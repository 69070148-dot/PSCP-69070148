"""ส่งต่อ"""

n, s = map(int, input().split())
a = []

for _ in range(n):
    a.append(int(input()))

visited = [False] * (n + 1)
count = 0

while s and not visited[s]:
    visited[s] = True
    count += 1
    s = a[s - 1]

print(count)
