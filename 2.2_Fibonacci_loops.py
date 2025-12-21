# Fibonacci series
n = int(input("Enter the number of terms:\t"))

a, b = 0, 1

if n <= 0:
    print("Please enter a positive integer.")
else:
    print("Fibonacci series up to",n, "terms:")
    print(a)
    print(b)
    i=1
    for i in range(n-2) :
        sum=a+b
        print(sum)
        a=b
        b=sum




































     
