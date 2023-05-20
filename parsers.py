def parse(feet_inches):
    separate_numbers = feet_inches.split()
    feet = float(separate_numbers[0])
    inches = float(separate_numbers[1])
    return {'feet': feet, 'inches': inches}
