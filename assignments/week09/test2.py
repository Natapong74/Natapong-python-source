try:
    num0 = int(input("Input number0: "))
    num1 = int(input("Input number1: "))
    operation = input("Mark (+,-,*,/): ")

    result = 0
    if operation == "+":
        result = num0 + num1
    elif operation == "-":
        result = num0 - num1
    elif operation == "*":
        result = num0 * num1
    elif operation == "/":
        result = num0 / num1
    else:
        raise ValueError("เครื่องหมายต้องเป็น +,-,*,/ เท่านั้น")
    
    print(f"{num0} {operation} {num1} = {result}")

except ValueError:
    print("กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")
except ZeroDivisionError:
    print("ไม่สามารถหารด้วยศูนย์ได้")
except Exception:
    print("ทำอะไรไม่ได้บางอย่างแต่ไม่แน่ใจว่าคืออะไร")
else:
    print("คำนวนข้อมูลเรียบร้อยแล้ว")
finally:
    print("จบการทำงาน")