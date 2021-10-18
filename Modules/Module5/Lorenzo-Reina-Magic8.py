import random
print(str('Welcome to Magic 8-Ball! '))
name = input(str('What is your name? '))
ebchoice = ['Yes - definetely.', 'It is decidedly so.', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say NO.', 'Outlook not so good.', 'Very doubtful.', 'You will die.', 'I hope you believe in miracles.', 'God may not be so merciful.']
question = input(str('What would you like to ask? '))
eboutcome = random.choice(ebchoice)
print(name + ' asks: ' + question + '... ' + eboutcome)