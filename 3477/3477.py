"""Pad thai"""

ingredients = {
    "Pad Thai Sauce", "Tofu", "Pickle Turnip", "Shrimp",
    "Bean Sprouts", "Noodle", "Chives", "Lime",
    "Egg", "Oil", "Peanuts"
}

flavors = {"Sweet", "Sour", "Salty"}

a = set()

while True:
    s = input()
    if s == "Cook":
        break
    a.add(s)

b = set()

while True:
    s = input()
    if s == "End":
        break
    b.add(s)

if not a.issubset(ingredients):
    print("This is not Pad Thai!!!")
elif a != ingredients:
    print("This is bad!")
elif b != flavors:
    print("Not Bad...")
else:
    print("Delicious!")
