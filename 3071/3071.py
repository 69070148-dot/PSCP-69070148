"""จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""

def main():
    """จำนวนในช่วง [A,B] ที่หารด้วย d เหลือเศษ r"""
    num1 = int(input())
    num2 = int(input())
    devided = int(input())
    remain = int(input())
    count = 0
    for i in range(num1,num2 + 1):
        if i % devided == remain :
            count += 1
    print(count)
main()
