# Arithmetic operations script

# Addition
a = 10
b = 5
sum_result = a + b
print("Sum:", sum_result)

# Subtraction
difference = a - b
print("Difference:", difference)

# Multiplication
product = a * b
print("Product:", product)

# Division
quotient = a / b
print("Quotient:", quotient)

# Modulus
remainder = a % b
print("Remainder:", remainder)

# Exponentiation
power = a ** b
print("Power:", power)
# String manipulation script

# Concatenation
str1 = "Hello"
str2 = "World"
concatenated_str = str1 + " " + str2
print("Concatenated String:", concatenated_str)

# String length
str_length = len(concatenated_str)
print("Length of String:", str_length)

# Accessing characters
first_char = concatenated_str[0]
last_char = concatenated_str[-1]
print("First Character:", first_char)
print("Last Character:", last_char)

# String slicing
substring = concatenated_str[1:5]
print("Substring:", substring)

# String methods
uppercase_str = concatenated_str.upper()
lowercase_str = concatenated_str.lower()
print("Uppercase String:", uppercase_str)
print("Lowercase String:", lowercase_str)# Conditional statements script

# if-else statement
num = 10
if num > 0:
    print("Number is positive")
else:
    print("Number is non-positive")

# if-elif-else ladder
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "D"
print("Grade:", grade)

# Nested if statement
num = 15
if num > 0:
    if num % 2 == 0:
        print("Number is positive and even")
    else:
        print("Number is positive and odd")
else:
    print("Number is non-positive")# Creating a list
my_list = [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  
print(my_list[-1])  

# Slicing
print(my_list[1:3])  
print(my_list[-1:2])

# Modifying elements
my_list[0] = 10
print(my_list)  

# Adding elements
my_list.append(6)
print(my_list) 

# Removing elements
my_list.remove(3)
print(my_list)  

# Length of the list
print(len(my_list))  





# Creating a dictionary
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing elements
print(my_dict['name'])  
print(my_dict.get('age')) 

# Modifying elements
my_dict['age'] = 31
print(my_dict)  

# Adding elements
my_dict['job'] = 'Developer'
print(my_dict)  

# Removing elements
del my_dict['city']
print(my_dict)  

# Checking existence of a key
if 'age' in my_dict:
    print("Age is present in the dictionary")






# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Accessing elements
print(my_tuple[0])  
print(my_tuple[-1])  

# Slicing
print(my_tuple[1:3])  

# Length of the tuple
print(len(my_tuple))  

# Tuple packing and unpacking
a, b, c = (10, 20, 30)
print(a, b, c)  

# Iterating through a tuple
for item in my_tuple:
    print(item)