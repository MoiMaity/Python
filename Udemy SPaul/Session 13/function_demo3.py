
def sum_digits(num):
    sum_d = 0
    num = abs(num)
    while num > 0:
        sum_d += num % 10
        num //= 10

    return sum_d
    print('Hello World!')


s = sum_digits(1234)
#print( num)
print(s)
s = sum_digits(-512)
print(s)