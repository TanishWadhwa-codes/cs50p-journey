#my first program in CS50 Python Course
#A
#ask user for it's name
name = input("What is your name?")

#greet the user with hello!
print("hello,")
print(name)


#B
#ask user for it's name
name = input("What is your name?")

# #greet the user with hello!
print("hello",name,sep='~')

#C
#ask user for it's name
name = input("What is your name?")

#greet the user with hello!
print("hello, \"friend\"")

#D
#ask user for it's name
name = input("What is your name?")

#greet the user with hello!
print(f"hello,\"{name}\"")
#E ( see in case 'E' if i accedently press excess space during input like i did , the output will show that space making it look not pleasing or messy but to fix it we use a method called ".strip()",as we did in 'F')
#ask user for it's name
name = input("What is your name?")

#greet the user with hello!
print(f"hello,{name}")

#F
#ask user for it's name
name = input("What is your name?")

#removes white space from string
name = name.strip()
#greet the user with hello!
print(f"hello, {name}")

#G
#ask user for it's name
name = input("What is your name?")

#capitalizes' the  first letter of string not all wprd's first letter , for this we use method called ".title()"
name= name.capitalize()
#greet the user with hello!
print(f"hello,{name}")

#H[in this we have used both methods i.e, strip and capitalize]
#ask user for it's name
name = input("What is your name?")

#removes excess space
name = name.strip()
#capitalize the  first letter of the string
name = name.capitalize()

#greet the user with hello!
print(f"hello,{name}")

# I
#ask user for it's name
name = input("What is your name?")
# #title it capitalize's  every first letter of the word in a string
name = name.title()
#greet the user with hello!
print(f"hello,{name}")

#J
#ask user for it's name
name = input("What is your name?")
# we can also chain methods , instead of just writing it over and over
name =name.strip().title()
#greet the user with hello!
print(f"hello,{name}")

#K
#ask user for it's name
#for the methods that we used up and the way we did that , there is a more neater and pleasent way to do that same work , decreasing the chances of mistakes
name = input("What is your name?").strip().title()

#greet the user with hello!
print(f"hello,{name}")

#L
#in case we want to split users first and last name down the middle we will use the method called (.split(""))
name = input("What is your name?").strip().title()
#to split in half the useer's name we use this:-
first ,last = name.split(" ")
#greet the user with hello!
print(f"hello ,Mr.{last}")
