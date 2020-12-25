cricket = {'India','England','Australia','New Zealand','Pakistan','Bangladesh','South Africa'}
soccer = {'England','India','Spain','Bangladesh','USA'}

either_or = cricket ^ soccer
print(either_or)

# only_cricket = soccer - cricket
# print(only_cricket)

# both = cricket & soccer
# print(both)

# either_or_both = cricket | soccer
# print(either_or_both)

x = {'a','b','c','d','e'}
y = set()



print(y.issubset(x))