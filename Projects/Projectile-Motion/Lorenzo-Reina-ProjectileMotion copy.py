import math 
from ExperimentalData import ExperimentalData 
from pathlib import Path
import json
import os

# gun = 'FN GL40'
# ammunition = '40x46 M381 mm Grenade'
# calibre = '40x46 M381 mm'
# FiringMode = 'Single'
# provel_ms = 76
# BuildingN = 'The Shard'
# BuildingH = 310
# g = 9.81

# Convert your variables into parameters

def ProjectileMotion(experimentalData:ExperimentalData):
  time_s= math.sqrt((2*experimentalData.BuildingH)/experimentalData.g)
  # distance_m= (experimentalData[provel_ms] *time_s)
  distance_m= (experimentalData.provel_ms*time_s)

  print(f"""The gun chosen was the {experimentalData.gun}. This weapon uses {experimentalData.ammunition} ammunition, and fires in a {experimentalData.FiringMode}-fire mode. The projectile velocity of the ammunition is {experimentalData.provel_ms} meters per second. The weapon will be fired from {experimentalData.BuildingH} meters, on top of {experimentalData.BuildingN}. """)

# Convert your script parameters into a single JSON object.
# experimentalData = {
# "gun":'FN GL40',
# "ammunition":'40x46 M381 mm Grenade',
# "calibre":'40x46 M381 mm',
# "FiringMode":'Single',
# "ProVel":76,
# "BuildingN":'The Shard',
# "BuildingH":310,
# "g": 9.81
# }

experimentalData = ExperimentalData('FN GL40', '40x46 M381 mm', '40x46 M381 Grenade', 76, 'Single', 'The Shard', 310, 9.81)

myDataSet = [
ExperimentalData('FN GL40', '40x46 M381 mm', '40x46 M381 Grenade', 76, 'Single', 'The Shard', 310, 9.81), 
ExperimentalData('Mosin', '7.62x54mmR', '7.62x54R LPS gzh', 927, 'Single', 'The Shard', 310, 9.81),
ExperimentalData('FN GL40', '40x46 M381 mm', '40x46 M381 Grenade', 76, 'Single', 'The Eiffel Tower', 324, 9.81),
ExperimentalData('Glock 17 9x19 pistol', '9x19 mm Prabellum', '9x19mm Pst gzh', 467, 'Single', 'The Shard', 310, 9.81),
ExperimentalData('Glock 17 9x19 pistol', '9x19 mm Prabellum', '9x19mm Pst gzh', 467, 'Single', 'The Eiffel Tower', 324, 9.81)
]

for data in myDataSet:
  print("\n---------------------------------\n")
  ProjectileMotion(data)

# Serialization
myOutputPath = Path(__file__).parents[0]
myOutputFilePath = os.path.join(myOutputPath, "Projectile-Motion.json")

with open(myOutputFilePath, 'w') as outfile:
  json.dump([data.__dict__ for data in myDataSet], outfile)
  # json.dump(myDataSet[0].__dict__, outfile)

# ProjectileMotion(experimentalData)