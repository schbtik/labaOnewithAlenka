class Maze:
    def __init__(self):
        self.grid = [
            list("###############"),
            list("#P........#...#"),
            list("#.#######.#.#.#"),
            list("#.#     #.#  .#"),
            list("#.# ### #.#  .#"),
            list("#.#   # #.GG..#"),
            list("#.### # #####.#"),
            list("#.....#.......#"),
            list("#####.#.#####.#"),
            list("#.....#.#    .#"),
            list("#.#####.# ## .#"),
            list("#.....#.# ## .#"),
            list("#.#####.####..#"),
            list("#O............#"),
            list("###############")
        ]

    def is_wall(self, x, y):
        """Перевіряє, чи є стіна на координатах (x, y)"""
        return self.grid[y][x] == '#'

    def is_point(self, x, y):
        """Перевіряє, чи є точка у комірці"""
        return self.grid[y][x] == '.'

    def is_power_pellet(self, x, y):
        """Перевіряє, чи є енергоджайзер у комірці"""
        return self.grid[y][x] == 'O'

    def eat_point(self, x, y):
        """З'їдає точку або енергоджайзер"""
        if self.grid[y][x] in ['.', 'O']:
            self.grid[y][x] = ' '  # Очистка клітинки
            return True
        return False


    def update_position(self, old_x, old_y, new_x, new_y, entity):
        """Оновлює розташування сутності (Pac-Man або привида) у лабіринті"""
        self.grid[old_y][old_x] = " "  # Очищаємо стару позицію
        self.grid[new_y][new_x] = entity  # Встановлюємо нову
        return 0
