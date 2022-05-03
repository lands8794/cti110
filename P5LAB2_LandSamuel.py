def feet_to_steps(feet):
    return int(feet/2.5)


if __name__ == '__main__':
    feet_walked = float(input())
    print(feet_to_steps(feet_walked))
