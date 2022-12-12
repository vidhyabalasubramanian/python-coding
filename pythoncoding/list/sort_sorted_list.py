# sorted vs sort()
numbers = ['a','e','d','c','b']
print(sorted(numbers)) # Sorts in temp memory
print(numbers)
print(numbers[1])
print(numbers.sort()) # Affects orginal memory
print(numbers) # prints origin memory ascending orders
print(numbers[1])# prints origin memory index

# sorted(reverse=True) vs reverse()
value1 = [5,10,15,20,25,30]
print(sorted(value1, reverse=True))
print(value1[1])
print(value1.sort())
print(value1)
print(value1.reverse())
print(value1)

#sorting string
val1 = ['10','10000','1000','100']
val1.sort()
print(val1)

alpha = ['a','b','d','e','c']
alpha.sort()
print(alpha)
print(alpha.reverse())
print(alpha)
