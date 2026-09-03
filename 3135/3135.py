"""ของขวัญและขโมย"""

def main():
    """ของขวัญและขโมย"""
    N, K, T = map(int, input().split())

    current = 1
    visited = set()
    count = 0

    while current not in visited:
        visited.add(current)
        count += 1

        if current == T:
            break

        current = (current + K - 1) % N + 1

    print(count)
main()
