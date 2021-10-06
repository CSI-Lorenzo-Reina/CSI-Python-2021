planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
g_ms2 = [3.7,8.87,9.81,3.711,24.79,10.44,8.69,11.1514]
print("Calculate your weight on all 8 planets!")
uWeight = int(input('What is your weight in pounds? : '))
uPlanet = input(f'On what planet would you like to be weighted on?: {planets} ')
print(('Your mass in kilograms on Earth is: ') + str(uWeight/2.204))
planet_index = planets.index(uPlanet)
print(f"Weight in {planets[planet_index]} is {((uWeight/2.204) * (g_ms2[planet_index])) / 4.45} lb.")