# Tried to make my solution better after understanding how modulo can be used

def rotate(sign, rotation, pointing_at, part1, part2):
    if sign == "-":
        rotation *= -1
    final = (pointing_at + rotation) % 100
    passed_0 = ((abs(pointing_at + rotation)) // 100)
    if final == 0:
        part1+=1
        part2+=1
    part2 += passed_0
    return final, part1, part2


if __name__=="__main__":
    file = open("day_1_input.txt") # Open file, split lines
    lines = file.read().split()
    pointing_at = 50  # Where the dial starts at
    part1, part2 = 0, 0
    for line in lines:
        sign = "+" if line[0] == "R" else "-"
        rotation = int(line[1:])
        pointing_at, part1, part2 = rotate(sign, rotation, pointing_at, part1, part2)

    print(f"Part1: {part1}")
    print(f"Part2: {part2}")