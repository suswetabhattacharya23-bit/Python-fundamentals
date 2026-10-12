# String Data Type
# Literal assignment
import math
first = "Susweta"
last = "Bhattacharya"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
Fullname = first + " " + last
print(Fullname)
Fullname += "!"
print(Fullname)

# Casting a number to a string
decade = str(2007)
print(type(decade))
print(decade)

statement = "I like rock music from " + decade + "s."
print(statement)

# Multiple lines
multiline = '''
Hey how are you?        
               
I was just checking in.   
                          All good?

'''
print(multiline)

# Escaping special characters
sentence = 'I\'m back at work!\tHey!\n\nWhere\'s this at\\located?'
print(sentence)

# String methods

print(first)
print(first.lower())
print(first.upper())
print(first)

print(multiline.title())
print(multiline.replace("good", "okay"))
print(multiline)

print(len(multiline))
multiline += "                                    "
multiline = "                            " + multiline
print(len(multiline))

print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))

print("")

# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "30 rupees".rjust(4))
print("Muffin".ljust(16, ".") + "50 rupees".rjust(4))
print("Cheesecake".ljust(16, ".") + "90 rupees".rjust(4))

print("")

# string index values
print(first[1])  # for second value because it starts with a 0
print(first[-1])  # for last value of the name
print(first[1:-1])
print(first[1:])

# Some methods return boolean data
print(first.startswith("S"))
print(first.endswith("a"))

# Boolean data type
myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))

# Numeric Data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))

# Float type
gpa = 8.85
y = float(1.04)
print(type(gpa))

# Complex type
comp_value = 5+3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)

# Built in functions for numbers
print(abs(gpa))
print(abs(gpa * -1))

print(round(gpa))
print(round(gpa, 1))


print(math.pi)
print(math.sqrt(68))
print(math.ceil(gpa))  # rounds up to narest integer
print(math.floor(gpa))  # rounds down to nearest integer

# Casting a string to a number
pincode = '700114'
pin_value = int(pincode)
print(type(pin_value))

# Error if you attempt to cast incorrect data
# pin_value = int("Kolkata")        #can't give incorrect data

 
