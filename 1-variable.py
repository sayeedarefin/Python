x="9" #it is a string
y=9 # it is an int
z=9.9 # it is a float
print(x)
print(y)
print(z)


########## Get the Type ###########
print(type(x))
print(type(y))
print(type(z))


#String variables can be declared either by using single or double quotes:

x = "sayeed"
x = 'sayeed'

##case sensitive
a= 4
A= 5
print(a)
print(A)

#Legal variable names:

# myvar = "John"
# my_var = "John"
# _my_var = "John"
# myVar = "John"
# MYVAR = "John"
# myvar2 = "John"

#Illegal variable names:

#2myvar = "John"
# my-var = "John"
# my var = "John"

# assign multiple value in multiple variable

x,y,z= 1,2,3
print(x)
print(y)
print(z)

#assign single value in multiple variable
x=y=z=900
print(x)
print(y)
print(z)

#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)


######################################
############# output variables ######

x="john"
y="doe"
z=500
print(x,y,z)
#print(x+y+z) #here python will give you an error

#############################
#Variables that are created outside of a function (as in all of the examples in the previous pages) are known as global variables.

globalVar = "too much"
def myFunc():
    print("Total cost is : " + globalVar)
myFunc()

print("Total cost is : " + globalVar)

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)

#Also, use the global keyword if you want to change a global variable inside a function.

p = "Dammam"
def function():
    global p # you have to tell the python first that it is a global variable, then it can be printed
    print(p)
    
    p = "zedda"

function()
print(p)

