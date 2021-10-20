print("Welcome to Simpsons' Shipping Co.")
uWeight= (float(input('How much does your package weigh? Please express in pounds. ')))
##GroundShipping
if uWeight == 2 or uWeight < 2:
    gsCost = ((uWeight*1.75)+20)
elif uWeight > 2 or uWeight <= 6:
    gsCost = ((uWeight*3.50)+20)
elif uWeight > 6 or uWeight <= 10:
    gsCost = ((uWeight*4.50) + 20)
elif uWeight > 10:
    gsCost =((uWeight*5.25)+20)
print(f'Ground Shipping would be ${gsCost}')
##CourierShipping 
if uWeight == 2 or uWeight < 2:
    csCost = ((uWeight*3.50)+5)
elif uWeight > 2 or uWeight <= 6:
    csCost = ((uWeight*7)+8)
elif uWeight > 6 or uWeight <= 10:
    csCost = ((uWeight*9)+12)
elif uWeight > 10:
    csCost =((uWeight*10.50)+15)
print(f'Courier Shipping would be ${csCost}')
##DroneShipping
if uWeight == 2 or uWeight < 2:
    dsCost = ((uWeight*5.25))
elif uWeight > 2 or uWeight <= 6:
    dsCost = ((uWeight*10.50))
elif uWeight > 6 or uWeight <= 10:
    dsCost = ((uWeight*13.50))
elif uWeight > 10:
    dsCost =((uWeight*15.75))
print(f'Drone Shipping would be ${dsCost}')
##PremiumGroundShipping
print('Premium Ground Shipping would be $150')