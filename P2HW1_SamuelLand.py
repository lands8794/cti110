# The program requests prices for five purchased items then calculates the subtotal, sales tax and overall
# total
#
# 20220219
# CTI-110 P2HW1 - Total Purchases
# Sam Land
#
#Pseudocode:
# 1) create a definition so this program can be called and is scalable
# 2) Initialize a blank dictionary to store user input values
# 3) initiate a for loop to iterate over each number in the range defined when calling the definition.
# 4) for each number, the for loop will get the price of the item from the user, and store it as a unique item in the
#    created dictionary
# 5) Once all items have been stored in the dictionary display the result using an f-string with the appropriate math
#    functions inserted to display the subtotal, sales tax and total.

def totals(x, y):
    d = {}
    for z in range(x, y):
        user_input = float(input(f'Enter the price of item #{z}: '))
        d[f'price_{z}'] = user_input

    print(f'''
-------Results-------
Subtotal:   {sum(d.values()):.2f}
Sales Tax:  {sum(d.values()) * .07:.2f}
Total:      {sum(d.values()) * 1.07:.2f}''')


totals(1, 6)
