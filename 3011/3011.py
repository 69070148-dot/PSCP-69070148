"""Colors"""

color1 = input().strip()
color2 = input().strip()

if color1 not in ["Red", "Blue", "Yellow"] or color2 not in ["Red", "Blue", "Yellow"]:
    print("Error")
elif color1 == color2:
    print(color1)
else:
    mix = {color1, color2}

    if mix == {"Red", "Yellow"}:
        print("Orange")
    elif mix == {"Red", "Blue"}:
        print("Violet")
    elif mix == {"Blue", "Yellow"}:
        print("Green")
    else:
        print("Error")
