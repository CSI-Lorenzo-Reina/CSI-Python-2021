# print('Hey there!')
# print("What's your name? ")
# myName = input()
# print('A pleasure to meet you, ',myName)
# print('How old are you, anyway?')
# myAge = input()
# print("You're gonna be " + str(int(myAge) + 5) + (" in 5 years!"))

print('Pyramid Volume Calculator')
print(''' 
                .
              /=\\
             /===\ \\
            /=====\' \\
           /=======\'' \\
          /=========\ ' '\\
         /===========\''   \\
        /=============\ ' '  \\
       /===============\   ''  \\
      /=================\' ' ' ' \\
     /===================\' ' '  ' \\
    /=====================\' '   ' ' \\
   /=======================\  '   ' /
  /=========================\   ' /
 /===========================\'  /
/=============================\/  
''')
l = int(input("What is the length of the pyramid?: "))
w = int(input("What is the width of the pyramid?: "))
h = int(input("What is the hight of the pyramid?: "))
print("The volume of the pyramid is", l*w*h*1/3)

def f(l,w,h):
    print(f"The volume of the pyramid is {int(l) * int(w) * int(h) * 1/3}")  
print('Length is 9.')
print('Width is 9.')
print('Height is 9')
f(9,9,9)