#for i in 'Hello Wor     ld This is a good example to understand continue':
#    if i == ' ':
#        continue
#    print (i, end = '*')

#print()
#print('Printing complete')


n = int (input('Enter a number: '))
i = 1
while i <= n:
    if i % 2 == 0:
        i = i + 1
        continue
    
    print (i, end = ' ')
    i = i + 1
    
print()    
print('At the end of while')    

