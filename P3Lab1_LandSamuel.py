color_1 = int(input())
color_2 = int(input())
color_3 = int(input())

list_1 = [color_1, color_2, color_3]

color_1 = color_1 - min(list_1)
color_2 = color_2 - min(list_1)
color_3 = color_3 - min(list_1)

print(color_1, color_2, color_3)
