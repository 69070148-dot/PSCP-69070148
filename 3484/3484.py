"""หุ่นยนต์เคาะเสียงกระเบื้อง"""

n, p = input().split()
n = int(n)
p = float(p)

a = []
rt = [0] * n
rp = [0] * n
ct = [0] * n
cp = [0] * n

tt = 0
tp = 0

for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        x = a[i][j]

        if x > 0:
            rt[i] += 1
            ct[j] += 1
            tt += 1

        rp[i] += x
        cp[j] += x
        tp += x

for i in range(n):
    print(*a[i], rt[i], rp[i])

print(*ct)
print(*cp)
print(tt, tp, format(tp * p, ".2f"))
