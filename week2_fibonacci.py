import time
def fib(n):
    if n <= 1:
        return n
    return fib(n-1)+fib(n-2)

def fibonacci3(n):

    a, b = 0, 1
    for i in range(1, n+1):
        a, b = b, a+b
    return b


for i in range(1,201):
    print("fib%d=%d"%(i,fibonacci3(i)))

start_time = time.clock()
end_time = time.clock()
print("fibonacci1: %f CPU seconds" % (end_time - start_time))