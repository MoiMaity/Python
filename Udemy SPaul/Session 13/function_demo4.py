def dummy(a):
    print("id of x: ", id(a))
    #print('x=', x, 'from function, before update')
    a = a + 1
    print("id of x: ", id(a))
    return a
    #print('x=', x, 'from function after update')


x = 10
print("id of x: ", id(x))
#print('x=',x,'Before calling function dummy')
x = dummy(x)
print("id of x: ", id(x))
#print('x=',x,'After calling function dummy')
