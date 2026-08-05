"""Ink"""

import math
def main():
    """Ink"""

    PI = 3.1416

    S, N = map(int, input().split())

    for _ in range(N):
        x, y = map(int, input().split())

        if not x and not y:
            print(0)
        else:
            t = PI * (x*x + y*y) / S
            print(math.ceil(t))
main()
