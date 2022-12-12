#for loop

values=[0,1,2,3,4,5]
print(len(values))
sum = 0
for num in values:
    sum+= num
print(values)

# while loop
#requirement need to print 1 to 15 values

value = 1
while value < 16:
    print(value)
    value += 1

num = 1
while num > 0:
    num+= 1
    if num ==5:
        continue
    if num ==15:
        break
    print(num) # 2 3 4 6 7 8 9 10 11 12 13 14