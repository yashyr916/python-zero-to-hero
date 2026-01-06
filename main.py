'''a = 5
b = 6
c = a + b
print(c)'''


# Program Number 2
'''length = int(input("Enter The Length Of Rectangle: "))
breadth = int(input("Enter The Breadth Of Rectangle: "))
area = length * breadth
print("area is ",area)'''

# Day 2

# Define functions for basic arithmetic operations
'''def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers, handling division by zero."""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    """Main calculator logic function."""
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    result = add(num1, num2)
                elif choice == '2':
                    result = subtract(num1, num2)
                elif choice == '3':
                    result = multiply(num1, num2)
                elif choice == '4':
                    result = divide(num1, num2)

                print(f"Result: {result}")
                break

            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                continue
        else:
            print("Invalid input. Please select a valid operation.")

if __name__ == "__main__":
    calculator()'''

#Day 3 Using if and Else Statements

'''a = int(input("enter number"))
b = int(input("enter number"))
if a-b>=0:
    print (a-b)
else:
    print(b-a)'''

'''n = int(input("Enter the number"))
if n%2==0:
    print("Even")
else:
    print("odd")
'''

# 🧠 PROBLEM: STUDENT RESULT CHECKER (IF–ELSE ONLY)
'''
a = str(input("Enter the Name"))
b = float(input("Enter the Number"))

if b<0 or b>100:
    print("Entered the Invalid Number")

elif b>=90:
    print(a, "You got Grade:A+")
elif b>=75:
    print(a, "You got Grade:A")
elif b>=60:
     print(a, "You got Grade:B")
elif b>=40:
     print(a, "You got Grade:C")
else:
    print("Sorry you are Fail")

'''

#Day 4 Check whther the Year is Leap Year or not

'''year = int(input("Enter Year"))

if year % 100 == 0:
    print("Leap Year")

elif year % 4 ==0:
    print("Leap Year")
else:
    print("Not a leap Year")'''

year = int(input("Enter Year"))

if year % 100 == 0:
    print("Leap Year")

elif year % 4 ==0:
    print("Leap Year")
else:
    print("Not a leap Year")