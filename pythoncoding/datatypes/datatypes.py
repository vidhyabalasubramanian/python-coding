a=5
print(a)
print(type(a))
b=1.5
print(b)
print(type(b))
c=True
print(c)
print(type(c))

# Everything in python is Object  ****Keep in mind always****

a = 10
print(a) # to know the value of a
print(type(a)) # to know the type of variable
print(id(a)) # to know the address of an abject

# int values
a = 10
print(a)

# Decimal form 
a = 0B1111 
print(a)

# octal form 
a = 0O123
b = 0O234
print(a)
print(b)

#Hexadecimal form
a = 0x10
b = 0X11
c = 0xFace
d = 0XBeef
print(a)
print(b)
print(c)
print(d)
word = 0xBeef # only A to F we can form in Hexaware
print(word)

#****Base Conversion Function****

"""3 inbuild func to convert one base to another"""
'''
bin()
oct()
hex()
'''
# oct convert to bin
a = bin(15)
b = bin(0o123)
print(a)
print(b)

# other base values converts to oct
A = oct(100)
B = oct(0b111101)
C = oct(0XFace)
print(A)
print(B)
print(C)
# other base values converts to hex
value1 = hex(1000)
value2 = hex(0b1001011)
value3 = hex(0o123456)
print(value1)
print(value2)
print(value3)

#float Datatype

a = 15.2
print(type(a))

# #floating values we have one Exponential forms/Scientific notation

f = 1.2e3 #1.2 * 10power3>1.2*1000> output 1200.0
print(f)
#method2
i = 1.2e16
print(i)

# complex datatypes

x = 10+20j
print(type(x))

print(x.real)
print(x.imag)

# Str with single,double & triple quotes

s = 'Hi'
print(s)
print(type(s))

s = "Hello"
print(s)
print(type(s))

C = "python class is very knowledgable!!!"
print(C)
a = '6"/ height'
print(a)

#Str with positive and negative index 

s = 'vidya'
print(s[0])
print(s[3])
print(s[-1])
print(s[-5])

#Str datatypes Slice Operator

alpha = 'abcdefghijklmnopqrstuvwxyz'
print(alpha[3:9])
print(alpha[:9]) # If you not specifing begin index default takes from 0 index
print(alpha[1:]) # If you not specifing end index until it will consider end of the string.
print(alpha[:]) # Didn't mention begin & end it will consider total string.
print(alpha[5:1]) # after 5 it will move forward only so you wont get 1 so get Empty String.

#Slice Operators Applications

s = 'vidya'
output = s[0].upper()+s[1:]  # First letter uppercase rest all lwercase
print(output)
output =s[:4]+s[4].upper() # Last letter uppercase reat all lowercase
print(output)

# METHOD2 => instead of hardcoding 4 we using lenof-1 so we can use code for any program.
output = s[0:len(s)-1]+s[-1].upper() 
print(output)

str = 'pythonlanguage'
output = str[0:len(str)-1]+str[-1].upper() 
print(output)
output = s[0:2]+s[2].upper()+s[3:] # Middle upper
print(output)
output = s[:].upper() # full str uppercase
print(output)
output = s[:].lower() # full str lowercase
print(output)

a = 'Hello'
output = a[0].upper()+a[1:5]+a[-1].upper()
print(output)

#Datatypes:+ and * operators for str type

# + operator
s = 'Hi'+'Hello' # Both argument should be Str
print(s)

# a = 'Hi'+10 # Both argument should be Str orelse will get type error
# print(a)

# * operator

s = "vidya", ''*3
print(s) 

print('#'*18)
print("WELCOME TO PYTHON")
print('#'*18)


