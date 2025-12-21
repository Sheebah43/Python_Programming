# Compute nth Fibonacci number without recursion

def main():
    n = int(input("Enter the number of terms:\n"))
    print(f"The Fibonacci series up to {n} terms is as:")

    a, b = 0, 1

    if n >= 1:
        print(a)
    if n >= 2:
        print(b)

    for i in range(0, n - 2):
        c = a + b
        print(c)
        a, b = b, c

if __name__ == "__main__":              
    main()
