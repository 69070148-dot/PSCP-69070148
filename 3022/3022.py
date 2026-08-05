"""Temperature"""

def main():
    """Temperature"""
    t = float(input())
    u = input()
    n = input()

    if u == "F":
        t = (t - 32) * 5 / 9
    elif u == "K":
        t -= 273.15
    elif u == "R":
        t = t * 5 / 9 - 273.15

    if n == "F":
        t = t * 9 / 5 + 32
    elif n == "K":
        t += 273.15
    elif n == "R":
        t = (t + 273.15) * 9 / 5

    print(f"{t:.2f}")
main()
