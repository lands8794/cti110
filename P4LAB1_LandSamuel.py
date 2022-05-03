user_text = input()

remove = (' ', '.', '!',',')

for character in remove:
    user_text = user_text.replace(character, '')

print (len(user_text))
