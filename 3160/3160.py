"""หาจำนวนเฉพาะ"""

def is_prime():
    """หาจำนวนเฉพาะ"""
    start , stop = map(int, input().split())

    total = 0
    prime_numbers = []
    for num in range(start, stop + 1):
        if num < 2:
            continue
        for i in range(2, num):
            if not num % i:
                break
        else:
            prime_numbers.append(num)
            total += 1
    if prime_numbers:
        print(*prime_numbers)
    print(f"Total primes: {total}")

is_prime()
