#slicing particular list
bike = ['Avenger', 'Royal-Enfield', 'Ducati', 'Harley-Davidson']
print(bike[:])
print(bike[1:2])
print(bike[0:3])
print(bike[-1])

#Slice Operators Applications
s = 'vidya'
output = s[0].upper()+s[1:]  # First letter uppercase rest all lowercase
print(output)
output =s[:4]+s[4].upper() # Last letter uppercase reat all lowercase
print(output)

# METHOD2 => instead of hardcoding 4 we using lenof-1 so we can use code for any program.
output = s[0:len(s)-1]+s[-1].upper() 
print(output)

str = 'pythoncourse'
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