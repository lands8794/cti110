# This program will take user input of number of students and people per pizza and return how many pizzas and the price
#  to feed them.
# CTI-110
# P3HW2 - Pizza Order
# Sam Land
# 20220310

# pseudocode:
# Retrieve number of students from the user and store the input as variable "students"
# Retrieve people per pizza and store it as variable "ppp"
# create if else structure. Test if ppp = 2,3 or 1.5.
# if ppp is valid divide student by ppp, round it up to the nearest whole number and store its value as pizzas
# multiply pizzas by $5 to get cost, then by 1.06 to add 6 percent sales tax
# Display the number of students, Pizzas needed, and price
# if ppp is invalid display invalid entry

def main():
    students = int(input('How many students do you want to order pizza for? '))
    ppp = input('Enter number of people per pizza (1.5, 2 or 3): ')


    if ppp == '2' or ppp == '3' or ppp == '1.5':

        pizzas = round(students / float(ppp))

        price = pizzas * 5 * 1.06

        print(f'''-------Pizza Order-------
Number of Students : {students}
Pizzas Needed : {pizzas}
Price ${price:.2f}
-------------------------''')

    else:

        print(f'''INVALID ENTRY!!!!
Should have entered 1.5, 2 or 3

Run Program Again''')


main()

