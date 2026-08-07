def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def calculate_rectangle_area(base,height):
    """Calculates and displays triangle area"""
    area = 0.5 * base * height
    print(f"triangle with base {base} and height {height} ")
    print(f"area = 0.5 * {base} * {height} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()


def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def square(n):
    """Returns the square of a number"""
    return n * n

print("Using return values in expressions:")
result = multiply(4, 5) + square(3)
print(f"multiply(4, 5) + square(3) = {multiply(4, 5)} + {square(3)} = {result}")
print()

#""" เขียน function ชื่อ create_user_profile ที่มีคุณสมบัติดังนี้:

#รับ parameters: username (จำเป็น), age (ค่าเริ่มต้น 18), premium (ค่าเริ่มต้น False)
#return string ที่จัดรูปแบบข้อมูลผู้ใช้
#รูปแบบ: "[username] (age: [age]) - [Premium User / Standard User]"

def create_user_profile(username,age=18,premium = False):
    user_type = "standart"

    if premium == True:
        user_type = "premium"


    return print(f"{username} (age: {age}) - {user_type}")

create_user_profile("Boomchoo",'40')
create_user_profile("Manee")
create_user_profile("Piti",'23',True)