# to find the cubical value for elements in the list
numbers = [1,2,3,4]
cubes = []
for num in numbers:
    cubes.append(num*num*num)
print(cubes)
#methos2
values = [1,2,3]
cubes = [num*num for num in values]
print(cubes)

#changing uppercase in list and append a additional string 
cars = ['bmw','jaquar','benz']
uppercase = [ cars.upper() + ' Luxury !!!' for cars in cars ]
print (uppercase)

#if statement to find the senior citizen age list
age = [18,35,60,70,80,75]
s_age = []
for age in age:
    if age >=60:
        s_age.append(age)
print(s_age)
#method2
age = [18,35,60,70,80,75]
s_age = [a for a in age if a>=60]
print(s_age)