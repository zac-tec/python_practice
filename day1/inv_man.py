"""
QUESTION 1: The Inventory Manager
You have two lists: items and stock.
Task: Create a dictionary where the item name is the key and the value is 
the stock count. However, if the stock is 0, the value should instead 
be the string "OUT OF STOCK".

Input:
items = ["Laptop", "Mouse", "Keyboard"]
stock = [5, 0, 12]

Expected Output:
{'Laptop': 5, 'Mouse': 'OUT OF STOCK', 'Keyboard': 12}
"""

# Write your code below:

items=list(input("Enter the items:").split())
stock=list((int(x) for x in input("Enter the stock:").split()))
inventory = {}
inventory=dict.fromkeys(items,0)
print(inventory)
for i in range(len(items)):
    if stock[i] == 0:
        inventory[items[i]] = "OUT OF STOCK"
    else:
        inventory[items[i]] = stock[i]
print(inventory)    