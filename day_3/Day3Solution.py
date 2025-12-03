def get_joltage(line, total):
    batteries = list(line)
    b1 = max(batteries[:len(batteries)-1])
    i = batteries.index(b1)
    for l in batteries[:i+1]:
        batteries.remove(l)
    b2 = max(batteries)
    return total + int(b1+b2)

if __name__=="__main__":
    file = open("day_3_input.txt") # Open file, split lines
    lines = file.read().splitlines()
    total = 0
    for line in lines:
        total = get_joltage(line, total)
    print(total)