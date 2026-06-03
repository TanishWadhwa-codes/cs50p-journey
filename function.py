# Here we are learning today functions , how to create them for doing certain tasks for our convinence
# the keyboard for functions is def [meaning define]
#A

def hello():
    print("Hello")

#above we have written ourselve  code to create owr own function that print hello
#to call this function we would do:-
hello()

#B
#now we will create a function that takes input from the user and displays hello and the user"s name as well
def hello(x):
    print(f"Hello , {x}")

# here python takes input from user and displays it with hello using function , python does this as we have assumed a parameter to do this called 'x' here , python takes value from name and thinks that name and x are same variable and display the output
name = input("What's your name :- ")
hello(name)

#C
#now we will create a function that takes input from the user and displays hello and the user"s name as well but incase user doesn't call the parameter , the function will automatically display world
def hello(x="world"):
    print(f"Hello , {x}")

# here python takes input from user and displays it with hello using function , python does this as we have assumed a parameter to do this called 'x' here , python takes value from name and thinks that name and x are same variable and display the output , but here the user forgot to call parameter , the function will automatically display world to cope up with it

hello()

#D
#now we will two functions , one main function and another secondary function[hello], so that once we have set main function first , so we can write another function anywhere in the file , so that when we call it , first it calls main function , which further calls hello function
def main():
    name = input("What's your name:- ")
    hello(name)

def hello(to="world"):
    print(f"Hello, {to}")

main()

# Scope refers to a variable only existing in the context in which you defined it.

#Return is a keyword that returns value in functions only
#E
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))


def square(n):
    return n * n #instead of n*n , there is also a function i.e, pow(n,2) , where n is number and 2 is raised to power

#here we call function main , which in return calls square function , to execute the program
main()
