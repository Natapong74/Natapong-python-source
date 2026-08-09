prices = []
print("Enter princes of 6 item")
for i in range(6):
    price = int(input(f"Item {i+1}: "))
    prices.append(price)
butget = int(input("Enter total butget: "))
bought_items = []
total_spent = 0
for i in range(len(prices)):
    price = prices[i]
    if total_spent + price <= butget:
        print(f"Item {i+1} = {price} -> buy")
        total_spent += price
        bought_items.append(price)
    else:
        print(f"Item {i+1} = {price} -> cannot buy")
print("Bought items: ",bought_items)
print("Total spent: ",total_spent)
print("Remaining butget",butget - total_spent)