import math 
from ExperimentalData import ExperimentalData 

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
    time_s= math.sqrt((2*BuildingH)/g)
  # distance_m= (experimentalData[provel_ms] *time_s)
    distance_m= (provel_ms*time_s)

print(f'''
The gun chosen was the {gun}, a grenade launcher. This grenade launcher uses {ammunition} ammunition, and fires in a {FiringMode}-fire mode.
The projectile velocity of the grenade is {provel_ms} meters per second. The grenade launcher will be fired from {BuildingH} meters, on top of {BuildingN}.
''')

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

experimentalData = ExperimentalData('FN GL40', '40x46 M381', '40x46 M381 Grenade', 76, 'Single', 'The Shard', 310, 9.81)
ProjectileMotion(experimentalData)