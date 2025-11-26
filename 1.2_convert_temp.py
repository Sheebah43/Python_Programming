def cel(celsius):
    fahrenheit = (celsius * 9/5) + 32 
    print (celsius, "degrees in Celsius in farenheit is", fahrenheit)
def far(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print (fahrenheit, "degrees in fahrenheit in celsius is", celsius)
temp = int (input("If temperature is in Celsius, enter 0, else enter 1\n"))
if temp==0:
    cel_value = float(input("Enter the temperature in Celsius\n"))
    cel(cel_value)
elif temp==1:
    far_value = float(input("Enter the temperature in Farenheit\n"))
    far(far_value)
else:
    print("Invalid input")