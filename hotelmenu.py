menu ={
    'Pizza':100,
    'Pasta':120,
    'Coffee':90,
    'Salad':70,
    'Burger':80
}
print("welcom to python restaurant")
print("Pizza : Rs100\nPasta : Rs120\nCoffee : Rs90\nSalad : Rs70\nBurger : Rs80")

order_total = 0

item_1 = input("enter the name of item  you want  to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"your item {item_1} has been added to your order")
else:
    print(f"Orederd item {item_1} is not avalibale yet!")

another_order = input("Do you want  to add another  item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item {item_2} has been added to order")
    else:
        print(f"orederd item {item_2} is not avalibale yet!")
print(f"The total amount of items to pay is {order_total}")

