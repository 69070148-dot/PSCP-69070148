"""สลากกินแบ่ง"""

a = input().split()
b = input().split()

letter1 = a[0]
num1 = a[1]

letter2 = b[0]
num2 = b[1]

prize = 0

if letter1 == letter2 and num1 == num2:
    prize = 1000000

elif num1 == num2:
    prize = 100000

else:
    if num1[-3:] == num2[-3:]:
        if letter1 == letter2:
            prize = 2000
        else:
            prize = 200

    if num1[-2:] == num2[-2:]:
        if letter1 == letter2:
            prize = max(prize, 1000)
        else:
            prize = max(prize, 100)

    if letter1 == letter2:
        prize = max(prize, 20)

print(prize)
