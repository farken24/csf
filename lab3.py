# lab 3

series = 'sum'
n = 2
fib = 0
a = 0
b = 1
j = n
total = 0
add = 0
if series == 'fibonacci':
    for i in range(n):
        a = b
        b = fib
        fib = a + b
    print "The "+str(n)+"th Fibonacci number is: "+str(fib)

elif series == 'sum':
    while (j > 0):
        add = (3 * j)
        j = j - 1
        total = total + add
    print total

else :
    print "invalid string"
    
