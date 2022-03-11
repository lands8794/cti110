# The program takes an integer from user and outputs a letter grade
# total
#
# 20220310
# CTI-110 P3HW1 - Debugging
# Sam Land
#

def main():
    # This program takes a number grade and outputs a letter grade.

    # system uses 10-point grading scale
    A_score = 90
    B_score = 80
    C_score = 70

    # TO DO: define the rest of the scores

    score = int(input('Enter grade: '))

    if score >= A_score:
        print('Your grade is: A')

    elif score >= B_score:
        print('Your grade is: B')

    elif score >= C_score:
        print('Your grade is: C')

    else:
        print('Your grade is: F')


# program start
main()
