#A
#this is the most basic way to print the elements of list line by line
students = ["Hermione","Harry","Ron"]

print(students[0])
print(students[1])
print(students[2])

#B
#here we are going to the same work we did up there but more sophisticated using loops
students = ["Hermione","Harry","Ron"]

for  student in students:
    print(student)

#len is a function in python which tells the length of the data type
#C
#we are gonna write the same code but this time in loop lists as range using len function
students = ["Hermione","Harry","Ron"]

for i in range(len(students)):
    print(i+1,students[i]) # we are also ranking

#dict
#it is a data type in python , it is just like real life dictionary

#D
#here is an example of dictionary data type
students ={
    "Hermione":"Gryffindor",
    "Harry":"Griffindor",
    "Ron":"Griffindor",
    "Draco":"Slytherin"
}

print(students["Hermione"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])

#E
students ={
    "Hermione":"Gryffindor",
    "Harry":"Griffindor",
    "Ron":"Griffindor",
    "Draco":"Slytherin"
}

for student in students:
    print(student, students[student], sep=":- ")


#F
#what if we wanna store more data
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus":"Jack Russell terrir"},
    {"name": "Draco", "house": "Slytherine", "patronus":None},
]

for student in students:
    print(student["name"], student["house"],student["patronus"],sep=" : ")


