"""Imposter"""

players = {}
dead = {}

while True:
    s = input().strip()
    if s == "Start":
        break

    s = s.replace("{", "").replace("}", "").replace('"', "")
    name, role = s.split(":")
    players[name.strip()] = role.strip()

while True:
    name = input().strip()
    if name == "End":
        break

    if name in players:
        dead[name] = players.pop(name)

count = 0
for role in players.values():
    if role == "Impostor":
        count += 1

print(count, "Impostor Remains")
print("***Alive***")
for name in sorted(players):
    print(name, ":", players[name])

print("***Dead***")
for name in sorted(dead):
    print(name, ":", dead[name])
