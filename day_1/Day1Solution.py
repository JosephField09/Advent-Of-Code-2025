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

def rotate(sign, rotation):
    """
    Rotates the dial by the input rotation.
    Makes sure the dial doesn't go beyond 99 or below 0.

    :param sign: Either + or -
    :param rotation: The amount to rotate by
    :return: What the dial is pointing at now
    """
    final = eval(str(pointing_at)+sign+str(rotation))
    while final > 99 or final < 0:
        if final > 99:
            diff = final - 99
            final = -1 + diff
        elif final < 0:
            diff = abs(final)
            final = 100 - diff
    return final

if __name__=="__main__":
    file = open("day_1_input.txt") # Open file, split lines
    lines = file.read().split()
    pointing_at = 50  # Where the dial starts at
    password = 0

    for line in lines:
        sign = "+" if line[0] == "R" else "-"
        rotatation = get_rotation(line)
        pointing_at = rotate(sign, rotatation)
        if pointing_at == 0:
            password += 1

    print(f"Password: {password}")