x = int(input ("Enter first number: "))
y = int(input ("Enter second number: "))
z = int(input ("Enter third number: "))

max = 0

if x > y and x > z:
    print('You are in if-block')
    max = x
elif y > z:
    print('In the elif-block')
    max = y
else:
    print('in the else-block')
    max = z
    
    
print('Maximum is: ', max)
print ('Thank you!!!')


    
    
    
    
    
    
    
    
    
