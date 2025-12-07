def get_accessed(g, r, c, replace):
    count = 0
    neighbours = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for row in range(r):
        for col in range(c):
            if g[row][col] == "@":
                accessible = 0
                for horizontal, vertical in neighbours:
                    neighbour_row, neighbour_col = row + horizontal, col + vertical
                    if (0 <= neighbour_row < row_count and 0 <= neighbour_col < col_count
                            and g[neighbour_row][neighbour_col] == "@"):
                        accessible += 1
                if accessible < 4:
                    g[row][col] = replace
                    count +=1
    return count

def get_removed(g, r, c):
    removed = 1
    total_removed = 0
    while removed > 0:
        removed = get_accessed(g, r, c, 'x')
        total_removed += removed
    return total_removed

if __name__=="__main__":
    file = open("day_4_input.txt","r") # Open file, split lines
    grid = [list(line.strip()) for line in file]
    row_count = len(grid)
    col_count = len(grid[0])
    part1 = get_accessed(grid, row_count, col_count, '@')
    part2 = get_removed(grid, row_count, col_count)
    print(f"Part 1: {part1}")
    print(f"Part 2: {part2}")
