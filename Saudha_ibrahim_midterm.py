
#Saudha Ibrahim

#Q1-Write a Python program to do arithmetical operations addition and division

num1 = int(input("Enter first number: "))

num2 = int(input("Enter second number:"))

# Addition

addition_result = num1 + num2

print(f"Addition: {num1} + {num2} = {addition_result}")

#Division

division_result=num1/num2

print(f"division: {num1} / {num2} = {division_result}")

# Power

power_result=num1**num2

print(f"power: {num1} ^ {num2} = {power_result}")

# Floor-Division

floor_division_result=num1//num2

print(f"floor division: {num1} // {num2} ={floor_division_result}")

# Q2- write a python program to fin the area of triangle

length=int(input("Enter the length of base of triangle:"))

height=int(input("Enter the height of the triangle:"))

area_of_triangle=(1/2)*(length)*(height)

print("The area of triangle is : ", area_of_triangle)

#Q3- Write a python program to convert celcius to fahrenheit

temp_in_celsius=float(input("Enter temperature in celsius : "))

temp_in_fahrenheit=(9/5)*(temp_in_celsius)+(32)

print(f"{temp_in_celsius} degrees Celsius is equal to {temp_in_fahrenheit} degrees fahrenheit ")

#Q4-Write a python program that returns all data types that werd written in class.

# int

a=10

print("The data type of 10 is ", type(a))

# Float
b=10.5

print("The data type of 10.5 is ", type(b))

# 'str'

c= "Hello World"

print("The data type of Hello World is ",type(c))

# bool

d=True

print("The data type of True is ", type(d))

# list
whole_numbers=[1, 2, 3, 4, 5]

print("The data type of [1, 2, 3, 4, 5] is ", type(whole_numbers))

# tuple

numbers=(1, 2, 3, 4, 5)

print("The data type of (1, 2, 3, 4, 5) is ", type(numbers))

# set
integers={1, 2, 3, 4, 5}

print("The data type of {1, 2, 3, 4, 5} is ", type(integers))

#dictionary

bio_data={"name":"Saudha","father":"ibrahim", "residential area":"karachi"}

print("The data type of personal_info is ", type(bio_data))