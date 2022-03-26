# The program requests an amount of grades to be input by the user and outputs the lowest grade, the list of grades
# without the lowest grade, the score average, and the letter grade of the average.
#
# CTI-110
# P4HW1 - Score List
# Sam Land
# 20220325

# Pseudocode:
# 1) create a definition so this program can be called
# 2) Ask the user how many scores they want to enter and store that as variable num_scores
# 3) create a variable for the number 1 to use to increment
# 4) Initialize a blank list to store user input values named score_list
# 5) initiate a for loop to iterate for every number in the range num_scores
# 6) for every number in the range, request the user enters a score
# 7) initiate a while loop to validate use's input is between 0 and 100
# 8) if value not in expected range, request input again
# 9) increment the num value
# 10) append the users input to the list
# 11) find the lowest entry
# 12) remove the lowest entry from the list
# 13) Find the average
# 14) Create an if statement to assign a letter grade to the letter_grade variable based on the score average
# 15) print the lowest score, modified list, score average, and letter grade


def scores():

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

    lowest_score = min(score_list)

    score_list.remove(lowest_score)

    score_avg = sum(score_list) / len(score_list)

    if score_avg < 70:
        letter_grade = 'F'
    elif score_avg < 80:
        letter_grade = 'C'
    elif score_avg < 90:
        letter_grade = 'B'
    else:
        letter_grade = 'A'

    print(f'''
-----------------Results-----------------
Lowest Score :  {lowest_score:.1f}
Modified List:  {score_list}
Score Average:  {score_avg:.2f}
Grade        :  {letter_grade}
-----------------------------------------''')


scores()
