a = float(input("Enter operand 1\n"))
b = float(input("Enter operand 2\n"))
op = int (input("For addition, enter 0\nFor subtraction, enter 1\nFor multiplication, enter 2\nFor division, enter 3\n"))
if op == 0:
    print(a,"+",b,"=",a+b)
elif op == 1:
    print(a,"-",b,"=",a-b)
elif op == 2:
    print(a,"*",b,"=",a*b)
elif op == 3:
    if b == 0:
        print("Invalid denominator")
    else:
        print (a,"/",b,"=",a/b)
else:
    print("Invalid input")