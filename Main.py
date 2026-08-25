


import json

with open("GameData/Units_V1.0/Reefback_IFV.json", "r") as file:
    units = json.load(file)

reefback = units

print(reefback["DisplayName"])
print(reefback["Health"]["MaxHP"])
print(reefback["Defense"]["Armor"])
print(reefback["Mobility"]["Speed"])

with open("GameData/Weapons_V1.0/30mm.json", "r") as file:
    weapons = json.load(file)
print(weapons["DisplayName"])
print(weapons["Damage"])
print(weapons["RateOfFire"])
print(weapons["Range"])