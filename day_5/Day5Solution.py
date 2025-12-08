def count_items(ingredients, ranges):
    count = 0
    for i in ingredients:
        for a,b in ranges:
            if a <= i <= b:
                count += 1
                break
    return count

def count_fresh_ids(ranges):
    ranges = sorted(ranges)
    merged = [ranges[0]]
    for a, b in ranges[1:]:
        if a <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], b))
        else:
            merged.append((a,b))
    return sum((b+1) - a for a, b in merged)

def main():
    file = open("day_5_input.txt", "r")
    content = file.read().split("\n")
    mid = content.index('')
    ranges = [tuple(map(int, line.split('-'))) for line in content[:mid]]
    ingredients = tuple(map(int, content[mid+1:]))
    part1 = count_items(ingredients, ranges)
    par2 = count_fresh_ids(ranges)
    print(f"Part 1: {part1}")
    print(f"Part 2: {par2}")

if __name__=="__main__":
    main()