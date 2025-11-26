num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))

if(num1>= num2) and (num1>= num3):
    largest = num1
elif(num2>= num1) and (num2>= num3):
    largest = num2
else:
    largest = num3
    print(f"the largest number is {largest}")
