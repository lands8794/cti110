from random import randint

# This program allows users to select between addition and subtraction of 2 random integers and test their answer
# against the correct answer

# 20220327
# CTI-110 P5HW2 - Math Quiz
# Sam Land
#
#
# Pseduo-code
#
# 1)  create a function named random_number that returns a Random Integer from 0 to 1000
# 2)  create a function named add that adds 2 integers passed to the function and returns their sum
# 3)  create a function named subtract that take 2 integers as arguments and subtracts integer 2 from 1 and returns the
#     result
# 4)  Create a function named math_quiz
# 5)  initialize variable menu that will display a menu of options
# 6)  initialize variable selection with '0'
# 7)  initiate a while loop that will continue until selection = 3
# 8)  print the menu and retrieve user input for a menu option
# 9)  initiate a while loop that validates user input, if input is not 1,2, or 3 pull another input from the user
# 10) initialize int_1 and int_2 with randomly generated numbers from the random_number function
# 11) initiate a if/elif/else. if selection equal '1' set the oper variable to '+' and pass integer 1 and 2 to the add
#     function and store the return as correct_answer
# 12) if selection equal '2' set the oper variable to '-' and pass integer 1 and 2 to the subtract function and store
#     the return as correct_answer
# 13) else (selection ='3') break the program
# 14) display the math equation and take user inputted answer to the math problem and store as student_answer
#     initiate while loop so the user can continue to try and answer the question until they get it right
# 15) compare the correct_answer with student answer, if correct display congratulations
# 16) if the user answer is too low, display that it is too low and have user try again
#     if the user answer is too high, display that it is too high and have user try again
#


def random_number():
    return randint(0, 1000)


def add(num_1, num_2):
    return num_1 + num_2


def subtract(num_1, num_2):
    return num_1 - num_2


def math_quiz():
    print('\nWelcome to Math Quiz\n')
    menu = f'''Main Menu
------------------------------
1) Adding Random Numbers
2) Subtracting Random Numbers
3) Exit\n'''

    selection = '0'
    while selection != '3':

        print(menu)
        selection = input("please enter a number from the menu above: ")

        while not (selection == '1' or selection == '2' or selection == '3'):
            selection = input(f'''INVALID ENTRY!!!!
please enter a VALID number from the menu above:''')

        int_1 = random_number()
        int_2 = random_number()

        if selection == '1':
            oper = '+'
            correct_answer = add(int_1, int_2)

        elif selection == '2':
            oper = '-'
            correct_answer = subtract(int_1, int_2)
        else:
            break

        print(f'''\n  {int_1}
{oper} {int_2}\n''')
        student_answer = int(input('Enter the correct answer:'))
        while student_answer != correct_answer:

            if student_answer < correct_answer:
                print(f'\nSorry, guess is too low.')
                student_answer = int(input('try again:'))
            else:
                print(f'\nSorry, guess is too high.')
                student_answer = int(input('try again:'))
        print("\nCongratulations! your answer is correct.\n")

    print(f'''\nThank you for playing...
Bye!!!''')


math_quiz()
