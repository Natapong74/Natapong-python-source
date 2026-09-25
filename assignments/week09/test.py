def calculate_eletricity_cost(units = 0):
    if units > 200:
        cost = (2.50*50) + (3.00 * 50) + (100* 3.5) + ((units - 200) * 4.00) + 25
        print("1-50 unit: 125.00 baht")
        print("51-100 unit: 150.00 baht")
        print("101-200 unit: 350.00 baht")
        print(f"201-{units} unit: {(units - 200) * 4.00} baht")
        print("Service charge: 25 baht")
        print("Total electricity bill:",cost)
    elif units > 100:
        cost = (2.50*50) + (3.00 * 50) + ((units - 100) * 3.50) + 25
        print("1-50 unit: 125.00 baht")
        print("51-100 unit: 150.00 baht")
        print(f"101-{units} unit: {(units - 100) * 3.50} bath")
        print("Service charge: 25 baht")
        print("Total electricity bill:",cost)
    elif units > 50:
        cost = (2.50*50) + ((units - 50) * 3.00) + 25
        print("1-50 unit: 125.00 baht")
        print(f"51-{units} unit: {(units - 50) * 3.00} baht")
        print("Service charge: 25 baht")
        print("Total electricity bill:",cost)
    elif units >= 0:
        cost = (2.50 * units) + 25
        print(f"1-{units} unit: {(2.50 * units)} baht")
        print("Service charge: 25 baht")
        print("Total electricity bill:",cost)
    else:
        print("จำนวนหน่วยไฟฟ้าที่ไม่ติดลบ")

print(" Program calculate eletricity bill ")

while(True):
    print("1.Eletricity bill amount")
    print("2.Exit program")
    choice = input("Select menu: ")

    if choice == "1":
        units = int(input("Amount eletricity: "))
        calculate_eletricity_cost(units)
    elif choice == "2":
        break
    else:
        print("Invalid choice")