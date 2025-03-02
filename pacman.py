class PacMan:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.lives = 3
        self.score = 0
        self.power_mode = False  # Чи активний енергоджайзер

    def move(self, direction, maze):
        """Переміщення Pac-Man у заданому напрямку"""
        new_x, new_y = self.x, self.y
        if direction == "UP":
            new_y -= 1
        elif direction == "DOWN":
            new_y += 1
        elif direction == "LEFT":
            new_x -= 1
        elif direction == "RIGHT":
            new_x += 1

        if not maze.is_wall(new_x, new_y):
            self.x, self.y = new_x, new_y
            if maze.eat_point(new_x, new_y):  # Якщо точка є – з'їдаємо
                self.score += 10
            if maze.is_power_pellet(new_x, new_y):  # Якщо енергоджайзер – активуємо режим
                self.power_mode = True



    def reset_position(self):
        # Сбросить Pac-Man в начальное положение
        self.x = 1  # Замените на ваши стартовые координаты
        self.y = 1  # Замените на ваши стартовые координаты
