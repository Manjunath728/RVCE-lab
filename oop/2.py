import time as t

def timeit(funct):
    def timed(*args,**kwargs):
        start=t.time()
        print("start time : ",start)
        res=funct(*args,**kwargs)
        end=t.time()
        print("end time : " ,end)
        print("Time taken :",end-start)
        return res
    return timed

@timeit
def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b

n=int(input("enter number of elements "))
f=fib()
for i in range(n):
    print(f.__next__())