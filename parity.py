#today we are going to use arithmetic operators
#A
#in this we take input from user and check if it's even or odd
x = int(input("What's the value of x :- "))
if x % 2 == 0:
    print(f"x is an even number")
else:
    print(f"x is an odd number")

#B
#in this code we are going to do the same thing as we did above but by now using functions
def main():
    x = int(input("What's the value of x :- "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()

#C
#here we are going to concise the above code
def main():
    x = int(input("What's the value of x :- "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):
    return True if n % 2 == 0 else False


if __name__ == "__main__":
    main()

#D
#here this it he most succinct version of the above code
def main():
    x = int(input("What's the value of x :- "))
    if is_even(x):
        print("EVEN")
    else:
        print("ODD")

def is_even(n):
        return (n % 2 == 0)


if __name__ == "__main__":
    main()



