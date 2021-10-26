gun = 'FN GL40'
cartridge = '40x46 mm'
FiringMode = 'Single'
ProVel = 76
BuildingN = 'The Shard'
BuildingH = 310
g = 9.81

def f(BuildingH,g):
    return ((2*BuildingH)/g)**1/2
print(f'For the 40x46mm grenade to reach the floor, it would take {f(BuildingH,g)} seconds.')
hdisp = f(BuildingH,g)

def f(ProVel,hdisp):
    return (ProVel*hdisp)
print(f'The 40x46mm grenade will touch down at {f(ProVel,hdisp)} meters from where it was fired.')

print(f'''
The gun chosen was the {gun}, a grenade launcher. This grenade launcher uses {cartridge} grenade ammunition, and fires in a {FiringMode}-fire mode.
The projectile velocity of the grenade is {ProVel} meters per second. The grenade launcher will be fired from {BuildingH} meters, on top of {BuildingN}.
''')
