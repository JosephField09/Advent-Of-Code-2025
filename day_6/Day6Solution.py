def find_total(content):
    lines = [line.split() for line in content]
    width = len(lines[0])
    total = 0
    for i in range(width):
        eq = ''
        for j in range(len(lines)-1):
            eq = eq + lines[j][i] + lines[-1][i]
        total += eval(eq[:-1])
    return total


def main():
    file = open("day_6_test.txt", "r")
    content = file.read().split("\n")
    part1 = find_total(content)
    print(part1)

if __name__=="__main__":
    main()