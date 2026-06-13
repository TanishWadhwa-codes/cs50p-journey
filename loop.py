#Week 2
#today we  are going to learn about loops to do repetitive tasks
#A[if i had to print meow 10 times then i would have to do this {without loop functions }, which is quite frustating]
print("meow")
print("meow")
print("meow")


# there are to blocks use for loops :- while loop and for loop
#while is a construct that allows us to ask a question again and again
#B
i = 3
while i != 0:
    print("meow")# if we leave this like this then it would run and may crash the code
    i = i-1

#C[if we want count upwards then:-]
i = 1
while i <= 3:
    print("meow")
    i = i+1

#D [now we will do the same thing but without equality sign in defining loop ]
i = 0
while i < 3:
    print("meow")
    i = i+1


#Lists are another type of  data types present in python, it is a way of containing multiple values all in same place, all in same variable

#For [as  we talked earlier there is also another type of loop called for loop]
#E[we have used for loop which will print meow 3 times with respect to the list]
for i in [0,1,2]:
    print("meow")

#F[here is a more compatible way to do the  same work , by using range function , in which we pass a value and it prints till the argument , not through it]
for i in range(1000):
    print("meow")

#G[there is also a way to do this without any loop]
print("meow\n" * 3, end="")

#H[we are gonna write a code , if we want to ask user a certain type of answer , that can be done by creating an infinite loop]
while True:
    n =int(input("What's the value of n?" ))
    if n>0:
        break#[it is used to break from a loop]

for _ in range(n):
    print("meow")

#I [it is a function that does same as a loop]
def main():
    number = get_number()
    meow(number)
def get_number():
    while True:
        n =int(input("What's the value of n?" ))
        if n > 0:
            break#{it breaks from the infinite loop}
    return n


def meow(n):
    for _ in range(n):
        print("meow")
main()
