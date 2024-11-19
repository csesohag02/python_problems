# Billing Item

## Instruction
Create a program calculates the total price of items that we want to buy.
When program starts it will display the list of item and price
Then program asks to select an item
Then based on user selected item, the program checks if the item exist in the store or not. Because when quantity of item is 0 then it is out of stock
Finally, if it is not out of stock we calculate total price of items and decrease quantity from the stock. This continues until user select 0. And when the loop is terminated the bill detail is printed to the console.

### Sample Output
```
========== Main Menu ==========
-------------------------------
id   item         price
1    computer     50000
2    monitor      20000
3    keyboard     1000
4    mouse        500
5    hdmi cable   100
6    dvd drive    300
-------------------------------
Note:
Enter id numbers for order!
Enter 0 for calculate total!
_______________________________

Order Item: 1
Quantity: 1
Order Item: 0

================== Bill Details ==================
--------------------------------------------------
id   item         price     quantity    ammount
1    computer     50000     1           50000
--------------------------------------------------
total amount:                           50000
__________________________________________________

Want to process another order?('Y/N'): y
Order Item: 2
Quantity: 2
Order Item: 0

================== Bill Details ==================
--------------------------------------------------
id   item         price     quantity    ammount
2    monitor      20000     2           40000
--------------------------------------------------
total amount:                           40000
__________________________________________________

Want to process another order?('Y/N'): n
```
