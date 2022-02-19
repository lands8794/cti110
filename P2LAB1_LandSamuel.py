user_int = int(input('Enter integer (32 - 126):\n'))
user_float = float(input('Enter float:\n'))
user_character = str(input('Enter character:\n'))
user_string = str(input('Enter string:\n'))

print(f'{user_int} {user_float} {user_character} {user_string}')
print(f'{user_string} {user_character} {user_float} {user_int}')

user_int_character = chr(user_int)

print(f'{user_int} converted to a character is {user_int_character}')
