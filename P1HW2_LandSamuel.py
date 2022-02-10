# This program will take user input of number of students and return how many pizzas and pizza slices will be needed to
# feed them.
# 20220210
# CTI-110 P1HW2 - Pizza Order
# Sam Land

# pseudocode:
# Retrieve number of students from the user and store the input as variable "students"
# multiply students by 3 to determine the number of pizza slices and store it as variable "slices"
# Divide students by 2 to determine the number of pizzas and store it as variable "pizzas"
# Display the number of students, slices, and pizzas needed


students = int(input('How many students do you want to order pizza for? '))

slices = students * 3
pizzas = students / 2

print(f'''-------Pizza Order-------
Number of Students : {students}
Pizza Slices Needed: {slices}
Pizzas Needed : {pizzas}
-------------------------
''')
