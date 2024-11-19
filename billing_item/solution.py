"""
Created on Wed Nov 20 00:50:49 2024
@author: csesohag02
"""


#items details
items = {
    1: {"item": "computer", "price": 50000, "stock": 10},
    2: {"item": "monitor", "price": 20000, "stock": 8},
    3: {"item": "keyboard", "price": 1000, "stock": 5},
    4: {"item": "mouse", "price": 500, "stock": 0},
    5: {"item": "hdmi cable", "price": 100, "stock": 7},
    6: {"item": "dvd drive", "price": 300, "stock": 5},
    }

print("========== Main Menu ==========")
print("-------------------------------")
print(f"{'id':<5}{'item':<13}price")
for key, value in items.items():
    print(f"{key:<5}{value['item']:<13}{value['price']}")
print("-------------------------------")
print("Note:\nEnter id numbers for order!\nEnter 0 for calculate total!")
print("_______________________________\n")

while True:
    order_items = {}
    while True:
        order = int(input("Order Item: "))
        if order == 0:
            break
        if order in order_items:
            print("Already added!")
            continue
        quantity = int(input("Quantity: "))
        if items[order]["stock"] < quantity:
            print("Out of stock!")
            continue
        order_items[order] = {"item": items[order]["item"], "price": items[order]["price"], "quantity": quantity, "ammount": quantity * items[order]["price"]}
        items[order]["stock"] -= quantity
        
    print("\n================== Bill Details ==================")
    print("--------------------------------------------------")
    print(f"{'id':<5}{'item':<13}{'price':<10}{'quantity':<12}ammount")
    for key, value in order_items.items():
        print(f"{key:<5}{value['item']:<13}{value['price']:<10}{value['quantity']:<12}{value['ammount']}")
    print("--------------------------------------------------")
    order_ammounts = []
    for value in order_items.values():
        order_ammounts.append(value["ammount"])
    print(f"{'total amount:':<40}{sum(order_ammounts)}")
    print("__________________________________________________\n")

    if input("Want to process another order?('Y/N'): ").upper() != 'Y':
        break


