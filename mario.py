#A
for _ in range(3):
    print("#")

#B
#lets create a more abstract way to do this
def main():
    print_column(3)

def print_column(height):

    for _ in range(height):
        print("#")
   # print("#\n" * height, end="")

main()

#C
def main():
    print_row(4)

def print_row(width):
    print("?" * width)

main()


#D

def main():
    print_square(3)


def print_square(size):
    #for each row in square
    for i in range(size):

        #for each brick in row
        for j in range(size):

            #print brick
            print("#",ends="")

        print()

main()


#E
def print_square(size):
    for i in range(3):
        print( "#" *size )

  


