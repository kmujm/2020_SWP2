import time

def iterfibo(n):
    if n <= 1:
        return n
    prePreNum = 0
    preNum = 1

    for i in range(1,n):
        currentNum = prePreNum + preNum
        prePreNum = preNum
        preNum = currentNum

    return currentNum




def fibo(n):
    if n <= 1:
        return n
    return fibo(n - 1) + fibo(n - 2)


while True:
    nbr = int(input("Enter a number: "))
    if nbr == -1:
        break
    ts = time.time()
    fibonumber1 = fibo(nbr)
    fibots = time.time() - ts
    ts = time.time()
    fibonumber2 = iterfibo(nbr)
    iterfibots = time.time() - ts
    print("Fibo(%d)=%d, time %.6f" %(nbr, fibonumber1, fibots))
    print("InterFibo(%d)=%d, time %.6f" %(nbr, fibonumber2, iterfibots))
