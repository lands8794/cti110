# This program displays a menu of options and allows a user to enter a series of scores to obtain the lowest score,
# average scores, modified list and average grade of the scores inputted.

# 20220327
# CTI-110 P5HW1 - Score List
# Sam Land

# Pseudocode:
# 1) create a definition to get the scores
# 2) Ask the user how many scores they want to enter and store that as variable num_scores
# 3) create a variable for the number 1 to use to increment
# 4) Initialize a blank list to store user input values named score_list
# 5) initiate a for loop to iterate for every number in the range num_scores
# 6) for every number in the range, request the user enters a score
# 7) initiate a while loop to validate use's input is between 0 and 100
# 8) if value not in expected range, request input again
# 9) increment the num value
# 10) append the users input to the list
# 11) return the list as the output of the definition
# 12) create a definition to evaluate the scores that takes a score list as input
# 13) find the lowest entry and save it as variable lowest_score
# 14) remove the lowest entry from the list and save it as variable score_list
# 15) Find the average and store it as variable score_avg
# 16) Create an if statement to assign a letter grade to the letter_grade variable based on the score average
# 17) return lowest_score, scores, score_avg, letter_grade as the output
# 18) create a function named score_results
# 19) initialize variable menu with the input options
# 20) initialize variable selection with '0'
# 21) initiate a while loop that runs while selection does not equal 3
# 22) display the menu and retrieve input from the user
# 23) initiate while loop to validate user input, if input invalid (not equal to 1, 2, or 3) ask for input again
# 24) initiate if, elif, else. if selection equals "1" run get_scores, and store values as scores
# 25) if selection equals "2", validate scores has values or is (true). if not, send user back to main menu after
#     displaying error
# 26) If scores has scores in it, pass a copy to evaluate_scores and print the returned output
# 27) if the user selects 3, the while loops will terminate and print Goodbye


def get_scores():

    num_scores = int(input(f'How many scores would you like to enter?: '))

    num = 1

    score_list = []

    for score in range(num_scores):

        user_input = float(input(f'Enter score #{num}: '))

        while not 0 <= user_input <= 100:

            print(f'''INVALID score entered!!!!
Scores should be between 0 and 100''')

            user_input = float(input(f'Enter score #{num} again: '))

        num = num + 1

        score_list.append(user_input)

    return score_list


def evaluate_scores(scores):

    lowest_score = min(scores)

    scores.remove(lowest_score)

    score_avg = sum(scores) / len(scores)

    if score_avg < 70:
        letter_grade = 'F'
    elif score_avg < 80:
        letter_grade = 'C'
    elif score_avg < 90:
        letter_grade = 'B'
    else:
        letter_grade = 'A'

    return lowest_score, scores, score_avg, letter_grade


def score_results():
    menu = f'''
-----------MENU-------------
1) Create Score List
2) Display Results
3) Exit
----------------------------'''

    selection = '0'
    scores = ()

    while selection != '3':
        print(menu)
        selection = input("please enter a number from the menu above: ")

        while not (selection == '1' or selection == '2' or selection == '3'):

            selection = input(f''' INVALID ENTRY!!!!
please enter a VALID number from the menu above:''')

        if selection == '1':
            scores = get_scores()

        elif selection == '2':
            if not bool(scores):
                print(f'''The score list is empty!
Sending you back to the main menu.''')

            else:
                score_output = evaluate_scores(scores[:])
                print(f'''
-----------------Results-----------------
Lowest Score :  {score_output[0]:.1f}
Modified List:  {score_output[1]}
Score Average:  {score_output[2]:.2f}
Grade        :  {score_output[3]}
-----------------------------------------''')
        else:
            pass

    print('Goodbye!')


score_results()
