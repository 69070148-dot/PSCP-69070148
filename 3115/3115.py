"""Arcade of Time: Store Check"""

def main():
    """Arcade of Time: Store Check"""
    n, _ = map(int, input().split())

    diff = [0] * 1442

    for _ in range(n):
        start, stop = map(int, input().split())
        diff[start] += 1
        diff[stop] -= 1

    open_count = [0] * 1441
    current = 0

    for t in range(1441):
        current += diff[t]
        open_count[t] = current

    times = list(map(int, input().split()))

    print(*[open_count[t] for t in times])

main()
