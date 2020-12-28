
a_list = [1, 2, 3, 4, 5]
b_list = [10, 20, 30]

#c_list = [i * j for i in a_list for j in b_list if i * j <= 100]
c_list = [(i, j) for i in a_list for j in b_list]

print(c_list)