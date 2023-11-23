def get_adjacent_tiles(x, y, grid_length_x, grid_length_y):
    adjacent_tiles = []

    # Check each adjacent tile and add it to the list if it's within the grid boundaries
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < grid_length_x and 0 <= new_y < grid_length_y:
            adjacent_tiles.append((new_x, new_y))

    return adjacent_tiles
