#declaring variables
age = 21
print(age)
#data types-numeric(int,float,complex)and sequence(list,tuple,string,range,set,tuple and dictionary)
#integer
x = 10
print(type(x))
#float
y = 10.5
print(type(y))

# Complex
z = 3 + 4j
print(type(z))

#list
fruits = ["apple", "banana", "cherry"]
print(type(fruits)) 
print(fruits[0]) 
#string
name = "Alice"
print(type(name)) 

#boolean
is_active = True
is_completed = False
print(type(is_active))
#set
unique_numbers = {1, 2, 3, 4, 5}
print(type(unique_numbers))  # <class 'set'>
print(unique_numbers) 
#tuple
coordinates = (10, 20)
print(type(coordinates))  # <class 'tuple'>
print(coordinates[0])
#dictionary
person = {"name": "John", "age": 25}
print(type(person))  # <class 'dict'>
print(person["name"])

#operators
#arithematic operators
a = 5
b = 3
print(a + b)  # 8
print(a - b)  # 2
print(a * b)  # 15
print(a / b)  # 1.666...
print(a // b) # 1
print(a % b)  # 2
print(a ** b) # 125
#relational or comparision  operators
a = 5
b = 3
print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
#logical operators
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x) 
# assignment operator
x = 10
x += 5  # x = x + 5 → x = 15
print(x)

x -= 3  # x = x - 3 → x = 12
print(x)

x *= 2  # x = x * 2 → x = 24
print(x)

#bitwise operators
a = 5  # 0101 in binary
b = 3  # 0011 in binary

print(a & b)  # 1 (0101 & 0011 = 0001)
print(a | b)  # 7 (0101 | 0011 = 0111)
print(a ^ b)  # 6 (0101 ^ 0011 = 0110)
print(~a)     # -6 (~0101 = -0110)
print(a << 1) # 10 (0101 << 1 = 1010)
print(a >> 1) # 2  (0101 >> 1 = 0010)
#conditional statement-if,else, elseif
#if
x = 10
if x > 5:
    print("x is greater than 5")
#else
x = 2
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
#elseif
x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is less than or equal to 5")
#loop-while,for
# Iterating through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
#while
# Print numbers from 0 to 4
x = 0
while x < 5:
    print(x)
    x += 1  # Increment x
#jump statement-continue,break
# Using break to exit a loop
for i in range(5):
    if i == 3:
        break  # Exit the loop when i is 3
    print(i)
#continue
# Using continue to skip an iteration
for i in range(5):
    if i == 2:
        continue  # Skip when i is 2
    print(i)
#functions-define,calling, return statement
#def function_name(parameters):
    # Function code
    # Return a value (optional)
def greet():
    print("Hello, welcome to Python functions!")

greet()  # Calling the function
#parameter and arguments
def greet(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet("Alice", 30)  # Passing arguments
#return statement
def add(a, b):
    return a + b

result = add(3, 5)
print(result)
#inbuild functions
#print()
print("Hello, world!")
#len()
name = "Alice"
print(len(name))  # Length of the string
#type()
x = 10
print(type(x))  # Type of x
#int(),flost(),str()
x = "25"
y = int(x)  # Convert string to integer
print(type(y))  # Output: <class 'int'>
#sum()
numbers = [1, 2, 3, 4]
print(sum(numbers))  # Sum of numbers in the list
#min and max()
numbers = [10, 20, 30, 5]
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
#function literables-range
#range()
numbers = [10, 20, 30, 5]
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
#sorted-it is arrange the asscending order
numbers = [10, 20, 30, 5]
print(min(numbers))  # Output: 5
print(max(numbers))  # Output: 30
#reverse()
numbers = [1, 2, 3, 4]
print(list(reversed(numbers)))  # Reversed list
#filter()
numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))  # Output: [2, 4, 6]