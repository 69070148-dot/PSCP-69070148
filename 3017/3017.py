"""Bill"""

def main() :
    """Bill"""
    Bill = int(input())
    Charge = Bill * 0.1

    if Charge > 1000:
        Charge = 1000
    elif Charge < 50:
        Charge = 50

    Total = (Bill + Charge) + ((Bill + Charge) * 0.07)
    print(f"{Total:.2f}")

main()
