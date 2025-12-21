# Sum of numbers divisible by 3 up to 100
sum = 0
for x in range(1, 101):
    if x % 3 == 0:
        sum += x
        print(sum)

print("Sum of numbers divisible by 3 up to 100 is:", sum)
