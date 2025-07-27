def generate_maze(size, extra_paths=0.15):
    maze = [[WALL for _ in range(size)] for _ in range(size)]

    def carve_passages(x, y):
        directions = [(2, 0), (-2, 0), (0, 2), (0, -2)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < size - 1 and 1 <= ny < size - 1 and maze[ny][nx] == WALL:
                maze[ny][nx] = PATH
                maze[y + dy // 2][x + dx // 2] = PATH
                carve_passages(nx, ny)

    # Step 1: Generate perfect maze
    start_x, start_y = 1, 1
    maze[start_y][start_x] = PATH
    carve_passages(start_x, start_y)
    maze[size - 2][size - 2] = PATH

    # Step 2: Add extra paths to create loops
    for _ in range(int(size * size * extra_paths)):
        x, y = random.randrange(1, size - 1), random.randrange(1, size - 1)
        if maze[y][x] == WALL:
            # Only convert to PATH if it connects two existing paths
            neighbors = 0
            if maze[y - 1][x] == PATH: neighbors += 1
            if maze[y + 1][x] == PATH: neighbors += 1
            if maze[y][x - 1] == PATH: neighbors += 1
            if maze[y][x + 1] == PATH: neighbors += 1
            if neighbors >= 2:
                maze[y][x] = PATH

    return maze
