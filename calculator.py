#int stands for integer in python
#python provides various operators to carry out various kinds of calculations
#A
# x = 1
# y = 2

# z = x + y

# print(z)

#B
#now we are going to do the same work but using input function to get information from user
# x = input("What's the value of x:-")
# y = input("What's the value of y:-")
# #see here if type values like 1 for x and 2 for y , something like that , what do you think will happen , normally it should show 3 . but you will be suprised it would rather show 12 , which is quite absurding . it happens because the input here is not an integer but rather string , due to which python treats the arguments as string and just , say join [concatenates] them

# z = x + y

# print(z)

#C
#now we are going to correct the above code, by using int functions , we would typecast the x and y variable so that python could  add just  like we do in maths
# x = int(input("what's the value of x :- "))
# y = int(input("what's the value of y :- "))

# z = x + y

# print(z)

#D
#A floating point value is a real number that has a decimal point in it
# x = float(input("what's the value of x :- "))
# y = float(input("what's the value of y :- "))

# z = x + y

# print(z)

#E
#we also have a function to round up the number to nearest value as required by the user{round(number[, ndigits])} , as we can see the '[]' stands for something optional , in case user wants to round the number to some specific places like tenths, hunderths ,... .  if the your doesn't this , python automatially round up the number to nearest integer
# x = float(input("what's the value of x :- "))
# y = float(input("what's the value of y :- "))
# # here the value will be round up to the nearest integer
# z =round(x + y)

# print(z)

#F
#like if want to add commas between digit  after you know every three digits like standard , we can do this in python :-
x = float(input("what's the value of x :- "))
y = float(input("what's the value of y :- "))

z = round(x + y)
#we would do the work here in print function
print(f"{z:,}")
