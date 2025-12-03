def get_joltage(line, size):
    joltage = ""
    current = 0
    while len(joltage) < size:
        next = max(line[current:(len(line)-(size-len(joltage)))+1])
        joltage += next
        current = line.index(next, current)+1
    return int(joltage)

if __name__=="__main__":
    file = open("day_3_input.txt","r") # Open file, split lines
    lines = file.read().splitlines()
    part1 = 0
    part2 = 0
    for line in lines:
        part1 += get_joltage(list(line), 2)
        part2 += get_joltage(list(line), 12)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")