"""CuteCat CuteFox"""
import ast

total = int(input())
animal_type = {}

for _ in range(total):
    catfox = ast.literal_eval(input())

    for name, num in catfox.items():
        animal_type[num.strip()] = name.strip()

if "Fubuki" not in animal_type.values() and "Fox01" not in animal_type:
    animal_type["Fox01"] = "Fubuki"

if "Garfield" not in animal_type.values() and "Cat01" not in animal_type:
    animal_type["Cat01"] = "Garfield"

def kk(x):
    """riang num"""
    return int(x[3:])

cat = sorted((c for c in animal_type if c.startswith("Cat")), key=kk)
fox = sorted((f for f in animal_type if f.startswith("Fox")), key=kk)

print(f"Cat : {len(cat)}")
print(f"Fox : {len(fox)}")

for a in cat + fox:
    print(f"{animal_type[a]} : {a}")
