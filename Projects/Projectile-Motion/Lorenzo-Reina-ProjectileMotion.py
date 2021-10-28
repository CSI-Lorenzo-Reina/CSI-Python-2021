import math 

gun = 'FN GL40'
ammunition = '40x46 M381 mm Grenade'
FiringMode = 'Single'
ProVel = 76
BuildingN = 'The Shard'
BuildingH = 310
g = 9.81

def f(BuildingH,g):
    return ((2*BuildingH)/g)**1/2
print(f'For the the projectile to reach the floor, it would take {f(BuildingH,g)} seconds.')
distance = f(BuildingH,g)

def f(ProVel,distance):
    return (ProVel*distance)
print(f'The projectile will touch down at {f(ProVel,distance)} meters from where it was fired.')

print(f'''
The gun chosen was the {gun}, a grenade launcher. This grenade launcher uses {ammunition} ammunition, and fires in a {FiringMode}-fire mode.
The projectile velocity of the grenade is {ProVel} meters per second. The grenade launcher will be fired from {BuildingH} meters, on top of {BuildingN}.
''')

