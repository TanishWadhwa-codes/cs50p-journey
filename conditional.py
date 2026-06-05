#Week 1
#Today , we are going to learn about if , else ...i.e,coditional statements{allow you, the programmer, to allow your program to make decisions:}
#let us know about some comparison operators first:-
#> and < symbols are probably quite familiar to you.
#>= denotes “greater than or equal to.”
#<= denotes “less than or equal to.”
#== denotes “equals.” Note the double equal sign: a single equal sign assigns a value, whereas two equal signs compare values.
#!= denotes “not equal to.”
#A
#if statements
x = int(input("What's the value of x ?  "))
y = int(input("What's the value of y ?  "))

if x > y:
    print("x is greater than y")
if x > y:
    print("x is less than y")
if x == y:
    print("both x and y are equal")
# B
# elif
x = int(input("What's the value of x ?  "))
y = int(input("What's the value of y ?  "))

if x > y:
    print("x is greater than y")
elif x > y:
    print("x is less than y")
elif x == y:
    print("both x and y are equal")

# C
# Else
x = int(input("What's the value of x ?  "))
y = int(input("What's the value of y ?  "))

if x > y:
    print("x is greater than y")
if x > y:
    print("x is less than y")
else:
    print("both x and y are equal")

# D
# (or) it returns only boolean values,ie , it will work only if either condition is true or both conditions are true , but if both condition is false it will return false value, here we are going to use it to tell whether x is equal to y or not
x = int(input("What's the value of x ?  "))
y = int(input("What's the value of y ?  "))

if x > y or x < y :
    print("x is not equal to y ")
else:
    print("both x and y are equal")

#E
#here we are going to make the code more consice and sophisticated
x = int(input("What's the value of x ?  "))
y = int(input("What's the value of y ?  "))

if x !=  y:
    print("x is not equal to y")
else:
    print("both x and y are equal")

#F
#let's grading system , which gives out grade on the basis of your score
score = int(input("Score :- "))

if score >=90 and score <=100:
    print("Grade:-A")
elif score >=80 and score < 90:
    print("Grade:- B")
elif score >=70 and score < 80:
    print("Grade:- C")
elif score >=60 and score < 70:
    print("Grade:- D")
elif score >=50 and score < 60:
    print("Grade:- E")
else:
    print("Grade:- F")

#G
#now lets do the same thing we did up there , but let's do this using chaining comparison operators
score = int(input("Score :- "))

if 90<= score <=100:
    print("Grade:-A")
elif 80<= score < 90:
    print("Grade:- B")
elif 70<= score < 80:
    print("Grade:- C")
elif 60<= score < 70:
    print("Grade:- D")
elif 50<= score < 60:
    print("Grade:- E")
else:
    print("Grade:- F")
