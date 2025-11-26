number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0 and number % 7 == 0:
    print(f"{number} is divisible by 3, 5, and 7.")
else:
    print(f"{number} is NOT divisible by 3, 5, and 7.")
