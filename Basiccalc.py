'''
We are making a basic calculator
Our Calculator has the four elementary functions, addition, multiply, subtraction, and division
We will prompt three inputs from the user: two numbers and an operation
'''
# Print a menu prompting the user four options; one for each operand.
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

''' The variables we use to store the user's inputs '''
choice = (input("Choose an Operation(1/2/3/4)"))
num1 = int(input("Choose a number"))
num2 = int(input("Choose a second number"))

def add(x, y):
    return (x+y)

def multiply(x, y):
    ''' Multiply the integers the user inputs and return the value. '''
    return (x*y)

def divide(x,y):
    ''' Subtract the integers the user inputs and return the value. '''
    return(x/y)

def subtract(x,y):
    ''' Divide the integers the user inputs and return the value. '''
    return (x-y)


'''
insert your code here.
We need to create four situations, one for each operand
After the operand is chosen, we want to print out the answer
Account for if the user inputs something other than the operand
'''

if choice == "1":
    print(num1, "+", num2, "=", add(num1,num2))
elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1,num2))
elif choice == "4":
    print(num1, "/", num2, "=", divide(num1,num2))
else:
    printf("Not a valid operand")