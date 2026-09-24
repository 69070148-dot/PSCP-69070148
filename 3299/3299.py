"""แปลงดอกไม้"""

import math

L, N = map(int, input().split())

k = math.ceil((math.sqrt(8 * N + 1) - 1) / 2)

print(math.ceil(k / L))
