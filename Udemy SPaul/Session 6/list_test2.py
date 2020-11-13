my_list = [10, 30, 40, 30, 50, 30, 50, 30, 20]

# c = my_list.count(30)
# print(c)

# my_list.reverse()
# print(my_list)
# x = my_list.pop(2)
# print(my_list, x)

# while 30 in my_list:
#     my_list.remove(30)
#
# print(my_list)

# x = my_list.index(100)
# print(x)

target = 50
c = my_list.count(target)
start = 0
i = 1
while i <= c:
    indx = my_list.index(target, start)
    print(indx)
    start = indx + 1
    i += 1








