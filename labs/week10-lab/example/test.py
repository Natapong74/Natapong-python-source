 1.รับค่า text จากผุ้ใช่
 2.รับค่าอักรขระที่ต้องการค้นหาจากผู้ใช้
 3.แสดงผลจำนวนของอักรขระในข้อความ text

#ตัวอย่างหน้าจอ
 insert your text : Boonchoo jitnupong
 Charcter to find : 0
 5 letters 'o' found in 'Boonchoo jitnupong'

count = 0
text = 'Boonchoo jitnupong'
for letter in text:
    if letter == 'o':
        count += 1
print(f"{count} letters 'o' found in '{text}'" )

count = 0
text = input("insert your text :")
char = input("character to find :")
for letter in text:
    if letter == char:
        count += 1
print(f"{count} letters '{char}' found in '{text}'" )

#เขียนโปรแกรมตรวจสอบความแข็งแรง PASSWORD
#นิยามของ strong password คือ ยาวมากกว่า 8 ตัว ,มีอักขระ @ 1 ตัว,มีตัวเลข,มีตัวอักษร

#ตัวอย่างหน้าจอ
#insert your password: Boonchoo
#your password is not strong!

#insert your password: Test@123
#your password is strong

password = input("Insert your password:")
lenght = len(password)
words = password.split('@')
if len(words) > 1: 
    left = words[0].isalnum()
    right = words[1].isalnum()
else:
    left = False;
    right = False;

if lenght >= 8 and len(words)== 2 and left == True and right == True:
    print("Your password is strong")
else:
    print("Your password is not strong")


print("\n=== MEMBERSHIP TEST ===")
print("'a' in 'program':", 'a' in 'program')  
print("'at' not in 'battle':", 'at' not in 'battle')

print("Backslash example:")
print("Path: C:\\Users\\Python")

print("\nRaw string example:")
print("Normal: This is \\x61 \\ngood example")
print(r"Raw: This is \x61 \ngood example")

name = "ashish"
age = 8
print("Using %% formatting:")
print("name=%s and age=%d" % (name, age))
print("name=%s and age=%d" % ("ankita", 6))

print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Capitalize: {text.capitalize()}")

test_str = "Hello123"
print(f"\nValidation methods for '{test_str}':")
print(f"isalnum(): {test_str.isalnum()}")
print(f"isalpha(): {test_str.isalpha()}")
print(f"isdigit(): {test_str.isdigit()}")
print(f"isupper(): {test_str.isupper()}")
print(f"islower(): {test_str.islower()}")
