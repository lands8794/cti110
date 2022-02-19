# The program requests prices for five purchased items then calculates the subtotal, sales tax and overall total
#
# 20220219
# CTI-110 P2HW2 - Score Avg
# Sam Land
#
# Pseudocode:
# 1) create a definition so this program can be called and is scalable
# 2) Initialize a blank list to store user input values
# 3) initiate a for loop to iterate over each number in the range defined when calling the definition.
# 4) for each number, the for loop will get the score from the user, and append it to the list
# 5) create a variable to hold the lowest score found using the min function
# 6) use the remove function to remove the lowest score from the list
# 7) Display the lowest score, the modified list, and the score average using an f-string. The score average math can be
#    done in sequence by dividing the sum of the list by its length


def totals(x, y):
    l = []
    for z in range(x, y):
        user_input = float(input(f'Enter score #{z}: '))
        l.append(user_input)

    lowest_score = min(l)
    l.remove(lowest_score)

    print(f'''
-------Results-------
Lowest Score :  {lowest_score:.1f}
Modified List:  {l}
Score Average:  {sum(l) / len(l):.2f}''')


totals(1, 8)
