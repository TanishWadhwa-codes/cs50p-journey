#here we are going to learn to use match , which is  like a conditional statement
#A
name = input("What's your name? ")

if name == "Harry":
      print("Gryffindor")
elif name == "Hermione":
      print("Gryffindor")
elif name == "Ron":
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")

#B
#there  is a more concise way to write it
name = input("What's your name? ")

if name == "Harry" or name == "Hermione" or name == "Ron":
      print("Gryffindor")
elif name == "Draco":
      print("Slytherin")
else:
      print("Who?")

#C
#now wr are going to write the same code but , using match
name = input("What's your name? ")

match name:
    case "Harry":
      print("Gryffindor")
    case  "Hermione":
      print("Gryffindor")
    case"Ron":
      print("Gryffindor")
    case "Draco":
      print("Slytherin")
    case _:
      print("Who ?")

#D
#there is a more consice way to do this
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
      print("Gryffindor")
    case "Draco":
      print("Slytherin")
    case _:
      print("Who ?")


