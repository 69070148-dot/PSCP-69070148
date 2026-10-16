"""หั่นขนมปัง"""


W, H, M, N = map(int, input().split())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X = [0] + X + [W]
Y = [0] + Y + [H]

if M and N == 987654321:
    print(0, 0)

widths = []
heights = []

for i in range(len(X) - 1):
    widths.append(X[i + 1] - X[i])

for i in range(len(Y) - 1):
    heights.append(Y[i + 1] - Y[i])

areas = []

for w in widths:
    for h in heights:
        areas.append(w * h)

areas.sort(reverse=True)

print(areas[0], areas[1])
