def get_rotation(line):
    """
    Works out how much the dial should be rotated by.

    :param line: The input line (e.g. R67)
    :return: The amount the dial should be rotated
    """
    rotation = ""
    for l in line[1:]:
        rotation = rotation + l
    return int(rotation)

def rotate(sign, rotation, pointing_at, password):
    """
    Rotates the dial by the input rotation.

    :param sign: Either + or -
    :param rotation: The amount to rotate by
    :param pointing_at: Current number it's pointing att
    :param password: Current total of clicks to 0
    :return: What the dial is pointing at now
    """
    passed_0 = 0
    final = pointing_at
    for i in range(rotation):
        if sign == "+":
            final += 1
            if final > 99:
                final = 0
        else:
            final -= 1
            if final < 0:
                final = 99
        if final == 0:
            passed_0 += 1
    password += passed_0
    return final, password

if __name__=="__main__":
    file = open("day_1_input.txt") # Open file, split lines
    lines = file.read().split()
    pointing_at = 50  # Where the dial starts at
    password = 0
    for line in lines:
        sign = "+" if line[0] == "R" else "-"
        rotation = get_rotation(line)
        pointing_at, password = rotate(sign, rotation, pointing_at, password)

    print(f"Password: {password}")