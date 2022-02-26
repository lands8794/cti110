input_1 = input('Enter desired auto service:\n')

dict_1 = {'Oil change': 35, 'Tire rotation': 19, 'Car wash': 7}

if input_1 in dict_1.keys():
    print(f'''You entered: {input_1}
Cost of {input_1.lower()}: ${dict_1[input_1]}''')

else:
    print(f'''You entered: {input_1}
Error: Requested service is not recognized''')
