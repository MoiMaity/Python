# Inheritance using Python.

class X:
    def fun_x(self):
        print("fun of base class X")

class A(X):
    def fun_a(self):
        print('Fun of class A')

    def fun_x(self):
        print("overrided method fun_x in class A")


class B(X):
    def fun_b(self):
        print("Fun of class B")

    def fun_x(self):
        print("overrided method fun_x in class B")

class C(B, A):
    def fun_c(self):
        print('Fun of class C')


c = C()
print(C.__mro__)
c.fun_x()

