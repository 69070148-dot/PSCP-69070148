"""RGB Mixed"""

def rgb_mixed():
    """RGB Mixed"""
    r1, g1, b1 = map(int, input().split())
    r2, g2, b2 = map(int, input().split())
    r3 = (r1 + r2) // 2
    g3 = (g1 + g2) // 2
    b3 = (b1 + b2) // 2
    print(r3, g3, b3)
rgb_mixed()
