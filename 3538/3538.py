"""B - Fully pair?"""

s = input()
ans = ""

for c in s:
    if s.count(c) % 2 == 1 and c not in ans:
        ans += c

if not ans:
    print("fully paired")
else:
    print(ans)
