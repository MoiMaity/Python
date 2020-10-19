# Introduction to for loop
# It is a kind of for-each loop and used to iterate over a sequence
# or collection.


#for i in range (99, 90, -1):
#    print(i)


#for i in 'Hello World':
#    print(i, end = '#')

n = int (input('Enter a number: '))
sum = 0
for i in range (2, n+1, 2):
    print(i, end = ' ')
    sum = sum + i
    
print()
print('Sum is: ', sum)    
