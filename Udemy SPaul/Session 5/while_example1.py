# more example using while loop
# 1. Find sum of integers from 1 to n
# 2. Find sum of even integers and odd integers upto n
# 3. Find factorial of a number n

n = int (input ('Enter a positive integer: '))

#sum = 0
#i = 2
#while i <= n:
#    print(i, end = ' ')
#    sum = sum + i
#    i = i + 2
    
#print('sum is: ', sum)

p = 1
i = 1
while i <= n:
    p = p * i
    i = i + 1
print('Factorial is: ', p)
