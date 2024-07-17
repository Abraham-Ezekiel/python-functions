'''def myfunc(a,b):
	sum = a + b
	return(sum)
#myfunc(3,6)
a = int(input("enter a number: "))
b = int(input("enter a another number: "))
result = myfunc(a,b)
print(result)
'''
#when creating a function, we pass variable(s) called parameter(s) 
#when calling a function, we pass value(s) called arguments

#positional argument
'''
def great(name,age):
	print(f"hello {name}, you are {age} yrs old")
great('Ab',23) 
'''

'''
def diff(a,b):
	return(a-b)

def product(a,b):
	return(a*b)

def quotient(a,b):
	return(a/b)

dif=diff(2,4)
prod=product(5,7)
quot=quotient(4,5)

print(dif,prod,quot)

def calculator(a,b):
	return((a+b),(a-b),(a*b),(a/b))
	#return(a-b)
	#return(a*b)
	#return(a/b)

cal = calculator(3,6)
print(cal)
#positional only
def add(a,b,/):
	return(a*b)
print(add(3,5))
'''

'''
#keyword argument
def great(name,age):
	return(f"hello {name} you are {age} yrs old")
mygreat=great('Ab',age =23)
print(mygreat)
#keyword only
def great(*,name, age):
	return(f"hello {name} you are {age} yrs old")
print(great(name='Ak',age=25))
'''

'''
#default argument: this allows you to define default value for a parameter if not specified or passed
def add(a,b=4):
	return(a+b)
result = add(6)
print(result)
'''
#variable length argument and keyword variable length argument
#create a calculator using functions and conditional statement.(use variable length and keyword variable length argument).
def add(*nums):
	return(nums+nums+nums)
print(add(3,5,7)) 
