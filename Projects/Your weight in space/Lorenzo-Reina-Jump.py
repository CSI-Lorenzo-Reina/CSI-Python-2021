print('Jumping Distance on all 8 planets')
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
rel_grav = [2.65,1.11,1,2.64,0.40,0.94, 1.13, 0.88]
JumpDist= int(input('How much is your jumping distance (in inches) on Earth?: ')) / 35.37
uPlanet = input(str('On what planet would you like to calculate your jumping distance on?: '))
planet_index = planets.index(uPlanet)
print(f"Jumping distance in {planets[planet_index]} is {(JumpDist) * (rel_grav[planet_index])} meters.")
