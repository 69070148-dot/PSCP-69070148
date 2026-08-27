"""สงคราม...ส่งด่วน"""

def main():
    """สงคราม...ส่งด่วน"""
    start, end = input().split()
    weight = float(input())

    routes = {
        ("BKK", "CNX"): (10, 30),
        ("CNX", "UBP"): (15, 40),
        ("UBP", "BKK"): (20, 40),
        ("BKK", "PKT"): (25, 50),
        ("PKT", "CNX"): (30, 60),
        ("UBP", "PKT"): (40, 70)}

    key = (start, end)

    if key in routes:
        base_fee, weight_fee = routes[key]
        total = base_fee + weight * weight_fee
        print(f"{total:.2f}")
    else:
        print("Error")

main()
