"""หาร 10"""

n = int(input())
n = n - (n % 10)
while n >= 0 :
    if not n:
        print(n,end="")
    else:
        print(n,end=" ")
    n -= 10
