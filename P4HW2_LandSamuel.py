import math

# This program will take user input of number of students and people per pizza and return how many pizzas and the price
#  to feed them.

# CTI-110
# P4HW2 - Pizza Order
# Sam Land
# 20220310

# pseudocode:
# define a variable to use for while loop
# initiate while loop to track the status of variable "again"
# Retrieve number of students from the user and store the input as variable "students"
# Retrieve people per pizza and store it as variable "ppp"
# initiate a while loop to validate ppp is a valid input
# if ppp is invalid, retrieve a valid ppp from the user
# determine the amount of pizzas by dividing the amount of students by ppp and rounding it up
# multiply pizzas by $5 to get cost, then by 1.06 to add 6 percent sales tax
# Display the number of students, Pizzas needed, and price
# ask the user if they want to run the program again, if they enter the value 'y' the while loop will iterate


def main():

    again = 'y'

    while again == 'y':

        students = int(input('How many students do you want to order pizza for? '))
        ppp = input('Enter number of people per pizza (1.5, 2 or 3): ')

        while not (ppp == '2' or ppp == '3' or ppp == '1.5'):

            print(f'''INVALID ENTRY!!!!
    Should have entered 1.5, 2, or 3''')

            ppp = input('Enter number of people per pizza again. (1.5, 2 or 3): ')

        pizzas = math.ceil(students / float(ppp))

        price = pizzas * 5 * 1.06

        print(f'''-------Pizza Order-------
Number of Students : {students}
Pizzas Needed : {pizzas}
Price ${price:.2f}
-------------------------''')

        again = input('Would you like to run the program again (y for yes): ')


main()
