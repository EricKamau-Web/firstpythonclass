number=78 #integer
x=67.32 #float
greeting = "Hello there" #string
isPythonIntresting= True #Bool
devices = ["laptop","computer","tablet"] # list
browsers= ("opera","firefox","chrome","safari") #Tuple
countries={"kenya","sudan","rwanda"} # Set
student= {
    "firstname": "Tevin",
    "age" : 18,
    "course" : "MIT"
} # This is a dictionary

print(isPythonIntresting)
print(x)
print(greeting)
print(devices)
print(browsers)
print(countries)
print(student)
print(student["firstname"])
print(student["age"])
print(student["course"])

#Determining the datatype of a variable
print(type(devices))
print(type(student))

#typecasting is the process of converting one datatype to another

print(int(x))
print(float(number))