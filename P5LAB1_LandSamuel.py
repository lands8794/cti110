def laps_to_miles(user_laps):
    return user_laps * .25


if __name__ == '__main__':
    laps = float(input())
    print(f'{laps_to_miles(laps):.2f}')
