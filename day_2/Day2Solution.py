def is_invalid(line, p1, p2):
    """
    Splits up the code and:
    part 1: checks if the first half of the string
    is the same as the second half

    part 2: checks if each number can be made by
    repeating a substring of itself

    :param line: The range (e.g. ['11 - 22'])
    :param p1: The current total for part 1
    :param p2: The current total for part 2
    :return: The totals after calculation
    """
    codes = line.split("-")
    for code in range(int(codes[0]), int(codes[1])+1):
        code_str = str(code)
        mid = len(code_str)//2
        if code_str[:mid] == code_str[mid:]:
            p1 += code
        for num in range(1, mid+1):
            reps = len(code_str)//num
            if code_str[:num] * reps == code_str:
                p2 += code
                break
    return p1, p2

if __name__=="__main__":
    file = open("day_2_input.txt")
    lines = file.read().split(",")
    part1, part2 = 0, 0
    for line in lines:
        part1, part2 = is_invalid(line, part1, part2)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")