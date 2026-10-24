"""isPrime_Large"""

n = int(input())

if n < 2:
    print("NO")
else:
    i = 2
    prime = True

    while i * i <= n:
        if not n % i:
            prime = False
            break
        i += 1

    if prime:
        print("YES")
    else:
        print("NO")
