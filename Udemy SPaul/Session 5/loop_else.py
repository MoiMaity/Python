

# In Python we can associate else-block with loop
#
# for i in 'HelloWorld':
#     if i == ' ':
#         break
#     print(i, end='')
# else:
#     print()
#     print('I am else - block')

import math
n = int(input('Enter a number: '))

i = 2
while i <= math.sqrt(n):
    if n % i == 0:
        print('The number: ', n, 'is not a prime number')
        break
    i += 1
else:
    print(n, 'is Prime Number')


print('Thank you!!!')