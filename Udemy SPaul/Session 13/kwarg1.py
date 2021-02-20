# variable length argument passing in Python

def process( *args, **kwargs):
    #print(fixed)
    print(args)
    print(kwargs)


process(100, 1000, fixed=10, k1=1000)


